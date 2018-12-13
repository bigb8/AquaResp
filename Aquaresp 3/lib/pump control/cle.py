# import Flushy
import ctypes
import os,sys
import time
myp = os.path.dirname(__file__)

FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")
# FlushDLL = ctypes.WinDLL("flush.dll")
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)
# hn = FlushDLL.FCWGetHandle(f,0)
# serialnumber = FlushDLL.FCWGetSerialNumber(f,0)



#1;on/off
#2;Device number
#3;Channel



interface = f
devno = int(sys.argv[2])

channel = int(sys.argv[3]) + 16

do =int(sys.argv[1])

# devno = 0 

# channel = 16
# do = 0

flush = FlushDLL.FCWSetSwitch(interface,devno,channel,do)