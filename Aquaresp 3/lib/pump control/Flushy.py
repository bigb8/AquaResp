import ctypes
import os
import time
myp = os.path.dirname(__file__)
# print os.path.dirname(sys.argv[0])
FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")
# my_func = getattr(FlushDLL, '_my_func@0')

# my_func()
# a=0
# print ctypes.pointer(a)
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)
hn = FlushDLL.FCWGetHandle(f,0)
serialnumber = FlushDLL.FCWGetSerialNumber(f,0)
# print hn

interface = f
devno = 0
ch1 = 16
ch2 = 17
ch3 = 18
ch4 = 19
status = FlushDLL.FCWGetSeqSwitch(f,devno,ch1,0)
# print hn
# print f
# print g
# print "Serial", serialnumber

# status = FlushDLL.FCWResetDevice(f,0)
# print "Status: " , status
# flush = FlushDLL.FCWSetSwitch(f,devno,16,0)
def GiveDeviceInterface():
	global f,g
	return f,g
	
def FlipOn(interface,devicenumber,channel):
	flush = FlushDLL.FCWSetSwitch(interface,devicenumber,channel,1)
	
def FlipOff(interface,devicenumber,channel):
	flush = FlushDLL.FCWSetSwitch(interface,devicenumber,channel,0)
	
	
def FlipFlop(interface,devicenumber,channel):
	status = FlushDLL.FCWGetSeqSwitch(interface,devicenumber,channel,0)
	if status == 0:
		flush = FlushDLL.FCWSetSwitch(interface,devicenumber,channel,1)
	else:
		flush = FlushDLL.FCWSetSwitch(interface,devicenumber,channel,0)
		
		
def EmergencyFlush():
	global interface
	flush = FlushDLL.FCWSetSwitch(interface,0,16,1)
	# flush = FlushDLL.FCWSetSwitch(interface,0,17,1)
	# flush = FlushDLL.FCWSetSwitch(interface,0,18,1)
	# flush = FlushDLL.FCWSetSwitch(interface,0,19,1)
	
def EmergencyOff():
	global interface
	flush = FlushDLL.FCWSetSwitch(interface,0,16,0)
	flush = FlushDLL.FCWSetSwitch(interface,0,17,0)
	flush = FlushDLL.FCWSetSwitch(interface,0,18,0)
	flush = FlushDLL.FCWSetSwitch(interface,0,19,0)
# EmergencyFlush()
# EmergencyOff()
# flush = FlushDLL.FCWSetSwitch(f,devno,ch1,0)		
# flush = FlushDLL.FCWSetSwitch(f,devno,ch2,0)		
# flush = FlushDLL.FCWSetSwitch(f,devno,ch4,0)		
# flush = FlushDLL.FCWSetSwitch(f,devno,ch3,0)		

# while 1:
	# time.sleep(1)
	# flush = FlushDLL.FCWSetSwitch(f,devno,ch1,1)
	# time.sleep(10)
	# FlipFlop(f,devno,ch1)
	# time.sleep(1)
	# FlipFlop(f,devno,ch2)
	# time.sleep(1)
	# FlipFlop(f,devno,ch3)
	# time.sleep(1)
	# FlipFlop(f,devno,ch4)



# print flush
# ended = FlushDLL.FCWCloseCleware(f)