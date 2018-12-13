import Flushy
import ctypes
import os,sys
import time
myp = os.path.dirname(__file__)

FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)
interface = f
devno = 0
ch1 = 16
ch2 = 17
ch3 = 18
ch4 = 19
Flushy.FlipOff(interface,devno,ch1)