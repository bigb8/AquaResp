import os,sys,shutil,time,datetime
# import numpy as np
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
temppath = mainpath + os.sep +"temp" + os.sep
libp = mainpath + os.sep +"lib" + os.sep


def presentfolderFunc():
	mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
	temppath = mainpath + os.sep +"temp" + os.sep
	with open(mainpath+ os.sep +"temp" + os.sep+"presentfolder.txt",'r') as f:
		pf = f.read()
	slopefolder = pf+"All slopes" + os.sep
	expfolder = pf+"Experimental information" + os.sep
	return pf, slopefolder, expfolder 

def SetRun(period):
	with open(temppath + "runningexperiment.txt",'w') as f:
		period = f.write(period)

def FORCEMEASUREMENTEND():
	with open(temppath + "ENDPERIOD.txt",'w') as f:
		period = f.write(str(1))
		
def FORCEMEASUREMENTEND_REQ():
	with open(temppath + "ENDPERIOD.txt",'r') as f:
		period = f.readlines()
	if period[0] == str(1):
		print( "Forced end of period")
		# print period[0], type(period[0])
		with open(temppath + "ENDPERIOD.txt",'w') as f:
			period = f.write(str(0))
		return True
	
	return False
		
# FORCEMEASUREMENTEND_REQ()
		
def TjekRun():	
	with open(temppath + "runningexperiment.txt",'r') as f:
		period = f.read()
		
	if period =="0":
		amirunning = False
	else:
		amirunning = True
		
	return amirunning
	
def PrintPeriod(period):
	with open(temppath + "currentperiod.txt",'w') as f:
		period = f.write(period)
	
def TjekPeriod():	
	with open(temppath + "currentperiod.txt",'r') as f:
		period = f.read()
	return period
	
def ox2file(pO2_1,pO2_2,pO2_3,pO2_4,oxtime1):
	# reads oxygen from firesting and prints to lastpo2.txt
	with open(temppath + "lastpo2.txt",'w') as f:
		f.write("%s;%s;%s;%s;%s;"% (pO2_1,pO2_2,pO2_3,pO2_4,oxtime1))

def GetLastOxygen():
	# reads oxygen from firesting and prints to lastpo2.txt
	with open(temppath + "lastpo2.txt",'r') as f:
		all = f.read()
		
	# pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = all.split(";")
	
	pO2_1 = all.split(";")[0]
	pO2_2 = all.split(";")[1]
	pO2_3 = all.split(";")[2]
	pO2_4 = all.split(";")[3]
	oxtime1 = all.split(";") [-1]
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime1
		
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)	

def GetNumResp():
	with open(temppath + "numresp.txt",'r') as f:
		nr = int(f.readlines()[0])
	return nr
	
		
def CopyExperimentalInfo():
	#Copies relavant info from temp to experimental folder
	pf, slopefolder, expfolder = presentfolderFunc()
	for i in range(1,5):
		shutil.copyfile(temppath + "respirometer_" + str(i) + ".txt", expfolder + "respirometer_" + str(i) + ".txt" )

			
	shutil.copyfile(temppath + "experiment.txt", expfolder + "experiment.txt")
	shutil.copyfile(temppath + "timestampstart.txt", expfolder + "timestampstart.txt")
	shutil.copyfile(temppath + "water.txt", expfolder + "water.txt")
	shutil.copyfile(temppath + "numresp.txt", expfolder + "numresp.txt")

def SetTimeStartExperiment():
	with open(temppath + "timestampstart.txt",'w') as f:
		f.write("UNIX:"+ str(int(time.time())) + ";\n Datetime:10dec1986;")
		
		
def GetTimeStartExperiment():
	with open(temppath + "timestampstart.txt",'r') as f:
		UNIXtimestart = int(f.readlines()[0].split(":")[1].split(";")[0])
	unixtimenow = int(time.time())
	in_seconds =  unixtimenow - UNIXtimestart
	in_hours = in_seconds / 3600.0
	in_minutes = in_seconds / 60.0
	in_days = in_seconds / 86400.0
	# print unixtimenow
	return in_hours, in_minutes,in_seconds, in_days

def updateLastmo2file(last,mo2,r2):
	if last ==1:
		with open(temppath + "lastmo2.txt","a") as f:
			f.write("\n")
		with open(temppath + "lastr2.txt","a") as f:
			f.write("\n")
	elif last == 2:
		with open(temppath + "lastmo2.txt","w") as f:
			f.write("")		
		with open(temppath + "lastr2.txt","w") as f:
			f.write("")
	else:
		with open(temppath + "lastmo2.txt","a") as f:
			f.write("%s;" % mo2 )		
		with open(temppath + "lastr2.txt","a") as f:
			f.write("%s;" % r2 )
			
	
def SetperiodStart(start,duration):
	with open(temppath + "timer.txt",'w') as f:
		f.write(str(start) + ";" + str(duration) + ";" )

def GetperiodStart():
	with open(temppath + "timer.txt",'r') as f:
		all = f.read().split(";")
	return int(all[0]),int(all[1]),int(time.time())-int(all[0])
	
	
def readrespirometerinfo(ch):
	#As function name says
	with open(temppath + "respirometer_" + str(ch) + ".txt","r") as f:
		lines = f.readlines()
		
	inuse = lines[0].split(":")[1].split(";")[0]
	volume = lines[1].split(":")[1].split(";")[0]
	animalmass = lines[2].split(":")[1].split(";")[0]
	
	return inuse, volume, animalmass
	
def GetExperimentInfo():
	#As function name says
	with open(temppath + "experiment.txt","r") as f:
		lines = f.readlines()
		
	sensor = lines[0].split(":")[1].split(";")[0]
	AD = lines[1].split(":")[1].split(";")[0]
	ExpType = lines[2].split(":")[1].split(";")[0]
	ft = lines[3].split(":")[1].split(";")[0]
	wt = lines[4].split(":")[1].split(";")[0]
	mt = lines[5].split(":")[1].split(";")[0]
	IsSlave = 'yes'
	
	with open(temppath + "water.txt","r") as f:
		lines2 = f.readlines()
	
	temperature = lines2[0].split(":")[1].split(";")[0]
	salinity = lines2[1].split(":")[1].split(";")[0]
	o2sol = lines2[2].split(":")[1].split(";")[0]
	
	with open(temppath + "timestampstart.txt","r") as f:
		lines3 = f.readlines()
	
	UNIXtime = lines3[0].split(":")[1].split(";")[0]
	Dateime = lines3[1].split(":")[1].split(";")[0]
	
	
	return sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave

def datafileStop():
	for chan in range( 1, 5):
		myfile = temppath  + "Summary data resp " + str(chan)+".txt"	
		inuse, volume, animalmass = readrespirometerinfo(chan)
		if inuse =="y":
			with open(myfile,"w") as f:
				f.write(" ")

	
	
	
def datafileinit():
	
	pf, slopefolder, expfolder = presentfolderFunc()
	sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol,UNIXtime, Dateime, IsSlave = GetExperimentInfo()
	
	ensure_dir(pf)
	ensure_dir(slopefolder)
	ensure_dir(expfolder)
	
	for chan in range( 1, 5):
		myfile = pf + os.sep + "Summary data resp " + str(chan)+".txt"	
		inuse, volume, animalmass = readrespirometerinfo(chan)
		if inuse =="y":
		
			with open(pf+"Summary data ABS resp " + str(chan)+".txt","a") as stxt1:stxt1.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;\n" % ("TimeStartMeasurement","In Hours","Unix time", "MO2", "Slope", "Intercept", "Pearson r", "R squared", "P value","respirometer"))
		
			with open(myfile,"w") as f:
				f.write("AQUARESP VERSION 3  ASAP - Data file "+"\n")
				f.write("--------------------------------------------------------------------------------------------------------------------------------\n")
				
				f.write("Experiment start, UNIX time: "+str(UNIXtime)+"\n")
				# f.write("Experiment Date and time: "+str(Dateime)+"\n")
				f.write("Flush time ,s: "+str(ft)+"\n")
				f.write("Wait time, s: "+str(wt)+"\n")
				f.write("Measurement time, s: "+str(mt)+"\n")
				f.write("Mass of fish, kg: "+str(animalmass)+"\n")
				f.write("Volume respirometer, L: "+str(volume)+"\n")
				f.write("Real volume (vresp - vfish) (neutrally bouyant), L: "+str(float(volume) - float(animalmass))+"\n")
				# f.write("Athmospheric pressure: "+str(patm)+"\n")
				f.write("Salinity: "+str(salinity)+"\n")
				f.write("Temperature: "+str(temperature)+"\n")
				f.write("Oxygen solubilty, mg O2 / L: "+str(o2sol)+"\n")	
				f.write("\n Timestamp is beginning of measurement period \n")
				f.write("-.-.-.-.-.-.-.-.------------------------------------------------------\n")
				f.write("Clock TIME;TIME HOURS;TIME UNIX;MO2;SLOPE;Intercept;Pearson R;R^2;P;Std Err; Measurement duration seconds;avg po2;median po2; minimum po2; max po2;delta po2;oxygen solubility;ratio vreal fish;total experiment duration hours;minutes;seconds;days;\n")

				
				
def GetsummaryData(ch):
	
	mo2 = []
	po2 = []
	r2 = []
	timesec = []
	num = []
	# print("CH ", ch)
	with open(temppath+"Summary data resp " + str(ch)+".txt","r") as stxt1:
		all = stxt1.readlines()
	i = 1
	for l in all:
		try:
			if l.split(";")[1][0] == "T": continue
			mo2.append(float(l.split(";")[3]))
			po2.append(float(l.split(";")[9]))
			timesec.append(float(l.split(";")[1]))
			r2.append(float(l.split(";")[5]))
			num.append(i)
			i+=1
		except IndexError: pass
		
	return mo2,po2,r2,timesec,num
				

def MO2Save(timestartmeasurement,in_hours,unixtime, MO2, slope, intercept, rr, r2, p_value, std_err, duration, avgpo2, medianpo2, minpo2,maxpo2, dpo2, beta, rRespFish, in_hours2, in_minutes,in_seconds, in_days,ch):

	pf, slopefolder, expfolder = presentfolderFunc()
	
	#"TIME;TIME HOURS;TIME UNIX;MO2;R^2;SLOPE;P;duration seconds;avg po2;median po2; minimum po2; max po2;delta po2;\n"
	with open(pf+"Summary data resp " + str(ch)+".txt","a") as stxt1:
		stxt1.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;\n" % (timestartmeasurement,in_hours,unixtime, MO2, slope,  intercept,  rr,  r2,  p_value,  std_err,duration, avgpo2, medianpo2, minpo2, maxpo2,  dpo2, beta, rRespFish, in_hours, in_minutes,in_seconds, in_days))
		
	with open(temppath+"Summary data resp " + str(ch)+".txt","a") as stxt1:
		stxt1.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;\n" % (timestartmeasurement,in_hours,unixtime, MO2,rr,  r2,  p_value,  std_err,duration, avgpo2, medianpo2, minpo2, maxpo2,  dpo2, beta, rRespFish, in_hours, in_minutes,in_seconds, in_days))
		
		
def MO2Save_TOT(timestartmeasurement,in_hours,unixtime, MO2, slope, intercept, rr, r2, p_value,ch):

	pf, slopefolder, expfolder = presentfolderFunc()
	#"TIME;TIME HOURS;TIME UNIX;MO2;R^2;SLOPE;P;duration seconds;avg po2;median po2; minimum po2; max po2;delta po2;\n"
	with open(pf+"Summary data ABS resp " + str(ch)+".txt","a") as stxt1:
		stxt1.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;\n" % (timestartmeasurement,in_hours,unixtime, MO2, slope, intercept, rr, r2, p_value,ch))
		
		
def CleanSummaryData():
	for i in range(1,5):
		print("Cleaning up ", i)
		try:
			with open(temppath+"Summary data resp " + str(i)+".txt","w") as stxt1:
				stxt1.write("")
		except: print ("No data")
	
	print("Moving files")
	pf, slopefolder, expfolder = presentfolderFunc()
	src = mainpath + "oxygen" + os.sep
	dst = pf + "Oxygen data raw" + os.sep
	if not os.path.exists(dst):
		os.makedirs(dst)
	
	for subdir, dirs, files in os.walk(libp):
		for file in files:
			# print(os.path.join(subdir, file))
			filepath = subdir + os.sep + file

			if filepath.endswith(".html"):	
				# print (filepath)
				os.remove(filepath)

		
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		shutil.copy(s, d)
	
