
# For use with Aquaresp.com
# Author: Morten Bo Soendergaard Svendsen, fishiology.dk/comparativ.com, April 2016


import sys,os
myp = os.path.dirname(os.path.realpath(__file__)) + os.sep
sys.path.append(myp + 'pump control')

import subprocess,filehandling

onoff = int(sys.argv[1]) #0:Off 1:On - MANDATORY

try:
	channel = sys.argv[2] #Channel number, optional
except: 
	channel = 0
	
try:
	devno = sys.argv[3] #Device number, optional
except: 
	devno = 0


#Get interface
my_interface = int(filehandling.GetExperimentInfo()[1])
print(my_interface)
# my_interface = 0
#my_interface = 0
## 0: Comparativ USB 1
## 1: Comparativ USB 4
## 2: Comparativ ADC
## 3: Measurement Computing 1208ls
## 4: Measurement Computing 1608



if my_interface == 0:
	## 0: Comparativ USB 1
	#1;on/off
	#2;Device number
	#3;Channel
	subprocess.Popen(["python",  myp + 'pump control'+os.sep +"cle.py",str(onoff),str(0),str(0)])
	# print devno,channel
	# print("CUSB")
		
		
if my_interface == 1:
	## 0: Comparativ USB 4
	#1;on/off
	#2;Device number
	#3;Channel
	subprocess.Popen(["python",  myp + 'pump control'+os.sep +"cle.py",str(onoff),str(devno),str(channel)])
		

	
	
if my_interface == 4:
	## 0: Comparativ ADC
	## Implement sysargs for channel control
	subprocess.Popen(["python",  myp + 'pump control'+os.sep+"phid.py",str(channel),str(onoff)])

		
		
		
if my_interface == 2:
	## 3: Measurement Computing 1208
	## Implement sysargs for channel control
	subprocess.Popen(["python",  myp + 'pump control'+os.sep+"mmc1208.py",str(onoff),str(0),str(0)])
	# print("MCC")



# Do
#subprocess.Popen(["python",  myp + 'pump control'+os.sep+"mmc1208.py",str(1),str(0),str(0)])
