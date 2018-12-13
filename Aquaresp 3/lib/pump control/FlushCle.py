import Flushy
import ctypes
import os
import time
from subprocess import Popen

myp = os.path.dirname(__file__)

FlushDLL = ctypes.WinDLL(myp + os.sep + "flush.dll")
f = FlushDLL.FCWInitObject()
g = FlushDLL.FCWOpenCleware(f)

interface = f
devno = 1
ch1 = 16
ch2 = 17
ch3 = 18
ch4 = 19


Flushy.FlipOn(interface,devno,ch1)


# Popen(["python",  myp +os.sep +"aupload.py"])