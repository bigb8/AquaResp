#Aquaresp pys
import aquarespdevice as aqdev
import filehandling
import AquaAnalyse as AA
#import AquaPlot
from subprocess import Popen
# Other
import os, time, datetime
import numpy as np
# import matplotlib.pyplot as plt
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
oxygenpath = mainpath + os.sep +"oxygen" + os.sep
temppath = mainpath + os.sep +"temp" + os.sep
fn = oxygenpath + "firesting.txt"
lib_p = mainpath  + os.sep + "lib" + os.sep



	
def MeasurementPeriod(mainpath):
	# fn = oxygenpath + "firesting.txt"
	# presentfolder 
	pf,slopefolder,expfolder = filehandling.presentfolderFunc()
	

	#Datacollection when it is measuring time
	measurementperiod1 = []
	measurementperiod2 = []
	measurementperiod3 = []
	measurementperiod4 = []
	timesec = []
	timeabs = []
	timeunix = []

	pO2_1,pO2_2,pO2_3,pO2_4,oxtime = ["","","","",""]
	oxtimeold = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
	unixtime = int(time.time())
	unixtime2 = int(time.time())
	timestartmeasurement = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
	timestartmeasurement2 = datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")


	datadict = {1:measurementperiod1,2:measurementperiod2,3:measurementperiod3,4:measurementperiod4}
	print( "Start Data Acquisition - MO2")
	
	while 1:
		try:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = aqdev.uniformoxygen()
		except:	
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = [0,0,0,0,datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")]
		# filehandling.ox2file(pO2_1,pO2_2,pO2_3,pO2_4,oxtime1)
		unixtime = int(time.time())
		# Standard sampling rate for Aquaresp is .25 second
		time.sleep(.25) 
		po2dict = {1:pO2_1,2:pO2_2,3:pO2_3,4:pO2_4}
		try:
			oxtime = datetime.datetime.strptime(oxtime1, "%H:%M:%S")
		except:
			print( "Missed a reading.")
			
		dtime = oxtime - oxtimeold
		stime = oxtime - timestartmeasurement
		
		if not dtime.total_seconds() == 0:
			# samplingrate in aquaresp is to high compared to the oxygenmeter. So if there is no time difference
			# between the samples, they are not logged.
			for i in range(1,5):
				# inuse, volume, animalmass = filehandling.readrespirometerinfo(i)	
				# if inuse =="y":
				try:
					datadict[i].append(float(po2dict[i]))
				except ValueError:
					datadict[i].append(float(9999))
				except:
					datadict[i].append(float(9998))
				
			timesec.append(float(stime.total_seconds()))
			timeabs.append(oxtime1)
			timeunix.append(unixtime)
			
			filehandling.ox2file(pO2_1,pO2_2,pO2_3,pO2_4,oxtime1)
			
		# print("her?",filehandling.TjekPeriod()	)
		oxtimeold = oxtime
		#When measurement period ends
		if filehandling.TjekPeriod() !="M":	break
		# 
		exp = filehandling.TjekRun()
		if not exp: break
	
	#Get measurement period duration
	duration = int(time.time()) - unixtime2
	
	#Handle save data, and MO2 Calculation etc
	numfiles = len([name for name in os.listdir(slopefolder) if os.path.isfile(os.path.join(slopefolder, name))])
	with open( slopefolder + "Cycle_" + str(numfiles + 1) + ".txt",'w')	as f:
		f.write("Time;Seconds from start for linreg;Unix Time;ch1 po2;ch2 po2;ch3 po2;ch4 po2;\n")
		for ii,l in enumerate(timesec):
			f.write("%s;%s;%s;%s;%s;%s;%s;\n"% (timeabs[ii],l,timeunix[ii],measurementperiod1[ii],measurementperiod2[ii],measurementperiod3[ii],measurementperiod4[ii]))
	
	measurementperiod1 = np.array(measurementperiod1)
	measurementperiod2 = np.array(measurementperiod2)
	measurementperiod3 = np.array(measurementperiod3)
	measurementperiod4 = np.array(measurementperiod4)
	datadict = {1:measurementperiod1,2:measurementperiod2,3:measurementperiod3,4:measurementperiod4}
	timesec = np.array(timesec)
	
	sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave = filehandling.GetExperimentInfo()
	filehandling.updateLastmo2file(2,"-","-")
	
	
	for ik in range(1,5):
		inuse, volume, animalmass = filehandling.readrespirometerinfo(ik)	
		
		if inuse =="y":
			slope, intercept, rr, p_value, std_err,avgpo2,medianpo2,minpo2,maxpo2 = AA.sloper(timesec,datadict[ik])
			in_hours, in_minutes,in_seconds, in_days = filehandling.GetTimeStartExperiment()
			MO2, beta, rRespFish,MO2_TOT = AA.mo2maker(slope,float(temperature),float(salinity),760,float(animalmass),float(volume))
			
			
			print( "Respirometer ", str(ik), "MO2: ", str(MO2), " r-squared: ",str(rr**2))
			filehandling.updateLastmo2file(0,MO2,rr**2)
			
			filehandling.MO2Save(timestartmeasurement2,in_hours,unixtime, MO2, slope, intercept, rr, rr**2, p_value, std_err,duration,avgpo2,medianpo2,minpo2,maxpo2, maxpo2-minpo2,beta,rRespFish,in_hours, in_minutes,in_seconds, in_days,ik)
			filehandling.MO2Save_TOT(timestartmeasurement,in_hours,unixtime, MO2_TOT, slope, intercept, rr,  rr**2, p_value,ik)
			
			
			try:	
				# AquaPlot.fakeJSdatasource()
				
			#Create copy data for  data viewer
				# Popen(["python",  mainpath +os.sep +"lib" + os.sep +"copytoGD.py"])
				Popen(["python",  mainpath +os.sep +"lib" + os.sep +"Plotz.py"])
				
			except: pass
	filehandling.updateLastmo2file(1,"-","-")
	
	
	Popen(["python", lib_p + os.sep + "Pump.py","1","0","1"])
	
	
	
def run():			

	# Firesting, Presens4, Fibox3, FNFiresting, FNFibox	= SensorMess()

	while 1:
		time.sleep(.25)
		if filehandling.TjekPeriod() =="M":
		#Initiate measurement period datacollection
			MeasurementPeriod(mainpath)
			break
run()
# Popen(["python", mainpath +os.sep +"lib" + os.sep +"copytoGD.py "])

