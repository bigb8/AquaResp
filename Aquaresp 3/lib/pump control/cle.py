# import Flushy
import ctypes
import os,sys
import time
myp = os.path.dirname(__file__)

FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")


#Ctypes Init - 64bit
FlushDLL.FCWInitObject.restype =  ctypes.c_void_p
FlushDLL.FCWOpenCleware.argtypes = [ctypes.c_void_p]
FlushDLL.FCWOpenCleware.restype = ctypes.c_int
FlushDLL.FCWSetSwitch.argtypes = [ctypes.c_void_p, ctypes.c_int,ctypes.c_int,ctypes.c_int]
FlushDLL.FCWSetSwitch.restype = ctypes.c_int
FlushDLL.FCWGetSwitch.argtypes = [ctypes.c_void_p, ctypes.c_int,ctypes.c_int]
FlushDLL.FCWGetSwitch.restype = ctypes.c_int


f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)


#1;on/off
#2;Device number
#3;Channel






interface = f
devno = int(sys.argv[2])
channel = int(sys.argv[3]) + 16
do =int(sys.argv[1])

flush = FlushDLL.FCWSetSwitch(interface,devno,channel,do)