

import time
import os, sys
# import Flushy
# import oxygenserver
import filehandling
from subprocess import Popen
import aquarespdevice as aqdev


#These functions provides experimental control over the flush pump, and writes to a text file what state the respirometer is in
# from multiprocessing import Process

myp = os.path.dirname(sys.argv[0])
main_p = myp.split("lib")[0]
temp_p = main_p + "temp"
lib_p = main_p + "lib"

# interface,deviceNo =  Flushy.GiveDeviceInterface()



	

def ConventionalIMF(tf,tw,tm):
#Experimental control for IMF starting with flush period. 
#Having only 1 channel to control the entire setup
	global interface
	devno = 0
	ch1 = 16

	# Flushy.EmergencyFlush()
	exp = True	
	while exp:	
		# Flushy.FlipOn(interface,devno,ch1)
		#Popen(["python", lib_p + os.sep + "Pump.py","1","0","1"])
		Popen(["py","-3", lib_p + os.sep + "Pump.py","1","0","1"])
		
		print( "Flush started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),ft)
		exp = filehandling.TjekRun()
		
		if not exp: break
		filehandling.PrintPeriod("F")
		
		time.sleep(tf)
		Popen(["py","-3", lib_p + os.sep +"oxygenserver.py"])
		#Popen(["python", lib_p + os.sep + "Pump.py","0","0","1"])
		Popen(["py","-3", lib_p + os.sep + "Pump.py","0","0","1"])
		
		
		# Flushy.FlipOff(interface,devno,ch1)
		print( "Waiting period started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),wt)
		filehandling.PrintPeriod("W")
		
		exp = filehandling.TjekRun()
		if not exp: break
		
		time.sleep(tw)
		
		print( "Measurement period started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),mt)
		filehandling.PrintPeriod("M")
		
		exp = filehandling.TjekRun()
		if not exp: break
		
		time.sleep(tm)
		
	Popen(["python", lib_p + os.sep + "Pump.py","1","0","1"])
	
	print( "Experiment End"	)
		
		
def ClosedStartIMF(tf,tw,tm):
#Experimental control for IMF starting with closed periods. 
#Having only 1 channel to control the entire setup
	global interface
	devno = 0
	ch1 = 16

	# Flushy.EmergencyFlush()
		
	while True:	
		Popen(["py","-3", lib_p + os.sep +"oxygenserver.py"])
		Popen(["py","-3", lib_p + os.sep + "Pump.py","0","0","1"])
		# Flushy.FlipOff(interface,devno,ch1)
		
		
		print( "Waiting period started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),wt)
		exp = filehandling.TjekRun()
		if not exp: break
		filehandling.PrintPeriod("W")
		time.sleep(tw)
		
		
		print( "Measurement period started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),mt)
		filehandling.PrintPeriod("M")
		exp = filehandling.TjekRun()
		if not exp: break
		time.sleep(tm)
		# Flushy.FlipOn(interface,devno,ch1)
		Popen(["py","-3", lib_p + os.sep + "Pump.py","1","0","1"])
		
		
		print( "Flush started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),ft)
		exp = filehandling.TjekRun()
		if not exp: break
		filehandling.PrintPeriod("F")
		time.sleep(tf)

		
def deltaPO2IMF(setp_dpo2,tf):
	#Starts with flush
	global interface
	devno = 0
	ch1 = 16

	Popen(["py","-3", lib_p + os.sep + "Pump.py","1","0","1"])
		
	while True:	
		#Popen(["py","-3", lib_p + os.sep +"pump control"+ os.sep+"FlushCle.py"])
		print( "Flush started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),ft)
		exp = filehandling.TjekRun()
		if not exp: break
		filehandling.PrintPeriod("F")
		
		
		# time.sleep(int(tf)-30)
		lf = 0
		while lf < int(tf):
			time.sleep(1)
			if filehandling.FORCEMEASUREMENTEND_REQ(): break
			lf += 1
		lf = 0
			
		# call calculator
		Popen(["py","-3", lib_p + os.sep +"oxygenserver.py"])
		
		exp = filehandling.TjekRun()
		if not exp: break
		
		# Stop flushing
		mandatorywait = 60
		Popen(["py","-3", lib_p + os.sep + "Pump.py","0","0","1"])
		
		
		
		print("Chamber closed: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		
		
		
		
		filehandling.SetperiodStart(int(time.time()),mandatorywait)
		filehandling.PrintPeriod("W")
		
		time.sleep(mandatorywait-30)
		
		print("Collecting data for start po2 -  30 sek to measurement start")
		# read po2 flush for 30 sec
		lf = 0
		sumpo2 = 0.0
		while lf < 30:
			# readpo2
			# readpo2,readpo22,readpo23,readpo24,oxtime = filehandling.GetLastOxygen()
			try:
				readpo2,readpo22,readpo23,readpo24,oxtime = aqdev.uniformoxygen()
			except:
				pass
			
			sumpo2 = sumpo2 + float(readpo2)
			time.sleep(1)
			lf+=1
		
		# get last wait po2 value
		po2flush = sumpo2 / 30.0
		print("Start pO2: ", po2flush)
		print("Flush On at pO2: ", po2flush - setp_dpo2)
		
		
		exp = filehandling.TjekRun()
		if not exp: break
		
		#change to po2 percent
		filehandling.SetperiodStart(int(time.time()),mt)
		filehandling.PrintPeriod("M")
		
		while True:
			# readpo2
			try:
				po2chamber,readpo22,readpo23,readpo24,oxtime = aqdev.uniformoxygen()
			except:
				pass
			
			#calc dpo2
			dpo2 = po2flush - float(po2chamber )

			# check if dpo2 > setpoint
			if dpo2 > setp_dpo2: break
			# true -> end
			
			#Waiting one second
			time.sleep(1)
			
			if filehandling.FORCEMEASUREMENTEND_REQ(): break
			
			exp = filehandling.TjekRun()
			if not exp: break
			
		filehandling.PrintPeriod("F")	
		
		
		
			
def adaptiveIMF(minpoints,r2lim):
		#Starts with flush
	global interface
	devno = 0
	ch1 = 16

	Popen(["py","-3", lib_p + os.sep + "Pump.py","1","0","1"])

	while True:
		print("Flush started: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),ft)
		exp = filehandling.TjekRun()
		if not exp: break
		filehandling.PrintPeriod("F")
			
		while True:
			# # # # # # #check flush dpo2 / dt
			pass
			
		# Stop flushing - wait is always nescessary
		Popen(["py","-3", lib_p + os.sep + "Pump.py","0","0","1"])
		print("Chamber closed: " + time.strftime("%Y-%m-%d %H:%M:%S"))
		filehandling.SetperiodStart(int(time.time()),30)
		filehandling.PrintPeriod("W")
		time.sleep(tw)
		
		# # # # # #Start new calculator, pass on minpoints
		
		while True:
			# check file for flush command
			if dpo2 > setp_dpo2: break # true -> end
			#Waiting one second
			time.sleep(1)
		

		
def closedrespirometry_uhuh(mo2interval):		
	global interface
	devno = 0
	ch1 = 16

	Popen(["py","-3", lib_p + os.sep +"pump control"+os.sep+"FlushCle.py"])
	
	print("Experiment starting in 60s, time is now " + time.strftime("%H:%M:%S"))
	filehandling.PrintPeriod("W")
	time.sleep(60)
	
	# Stop flushing - wait is always nescessary
	Popen(["python", lib_p + os.sep + "Pump.py","0","0","1"])
	print("Experiment started, time is now " + time.strftime("%H:%M:%S"))
	
	#init calculator and experiment time
	filehandling.PrintPeriod("W")
	
	# call calculator
	Popen(["python", lib_p + os.sep +"oxygenserver.py"])
	filehandling.SetperiodStart(int(time.time()),mo2interval)
	
	#wait one period before starting
	time.sleep(mo2interval)
	
	while True:
	
		exp = filehandling.TjekRun()
		if not exp: break
		
		#Start measuring
		filehandling.PrintPeriod("M")
		filehandling.SetperiodStart(int(time.time()),mo2interval)
		
		#wait interval
		time.sleep(mo2interval)
		
		#Set status to wait period to stop calculator
		filehandling.PrintPeriod("W")
	
		# A little wait period of 5 seconds to avoid using the same sensor values for following mo2 calculations
		time.sleep(5)
		
		# call calculator
		Popen(["python", lib_p + os.sep +"oxygenserver.py"])
		
		# And another one to be sure
		time.sleep(5)

	print("Experiment ended: flushing starts")
	global interface
	devno = 0
	ch1 = 16
	Popen(["python", lib_p + os.sep + "Pump.py","1","0","1"])

		
def Slave():
#Aquaresp acting as slave, listens to filehandling.TjekRun() for external setting of FWM status
	# Flushy.EmergencyFlush()
	exp = True	
	while exp:	
		whatperiod = filehandling.TjekPeriod()
		exp = filehandling.TjekRun()
		if not exp: break
		
		if whatperiod == "W":
			print("Wait period started" )
			# Popen(["python", lib_p + os.sep +"oxygenserver.py"])
			exp = filehandling.TjekRun()
			if not exp: break
			
		if whatperiod == "M":
			print("Measurement period registered")
			exp = filehandling.TjekRun()
			if not exp: break

		
		
		
		
	print( "Experiment End")
		

if __name__ == "__main__":		
	
	# update this
	exptype,ft,wt,mt,dpo2,mo2interval = sys.argv[1:]

	if int(exptype) == 0:
		#Conventional IMF, with flush started
		ConventionalIMF(int(ft),int(wt),int(mt))
		
	elif int(exptype) == 1:
		#MMR then SMR
		ClosedStartIMF(int(ft),int(wt),int(mt))
	
	elif int(exptype) == 2:
		#Delta pO2 flush
		# deltaPO2IMF(setp_dpo2,ft)
		deltaPO2IMF(4,ft)
	
	elif int(exptype) == 3:
		#Adaptive respirometry
		# adaptiveIMF(minpoints,r2lim)
		#TODO
		print( 'not implemented yet')
		
		
	elif int(exptype) == 4:
		# # Closed respirometry - baad boy / girl!
		closedrespirometry_uhuh(mo2interval)
		
	elif int(exptype) == 5:
		# # Slave setup
		Slave()
	

	
