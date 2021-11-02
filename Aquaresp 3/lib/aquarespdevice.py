from ctypes import WinDLL,c_long,c_int,byref
import os,filehandling
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
temppath = mainpath + "temp" + os.sep
oxypath = mainpath + os.sep + "oxygen" + os.sep


# # # #
def DigitalIO(bn,ch,state):
## Controls digital channels
	with open("C:\AQUARESP\Settings\OU_DLL.txt","r") as f:
		getdllstr = f.readlines()
	dllstr = getdllstr[0]
	USB1208dll = WinDLL(dllstr)
	# USB1208dll.cbFlashLED(0)
	USB1208dll.cbDOut(0,10,state) #Writes state to port
	Gadus = "Not relevant"
	return Gadus

def tail( f,window=1):
	#Reads only end of text tile

	BUFSIZ = 1024
	f.seek(0, 2)
	# f.seek(-6, 2)
	bytes = f.tell()
	size = window
	block = -1
	data = []
	while size > 0 and bytes > 0:
		if (bytes - BUFSIZ > 0):
			# Seek back one whole BUFSIZ
			f.seek(block*BUFSIZ, 2)
			# read BUFFER
			data.append(f.read(BUFSIZ))
		else:
			# file too small, start from begining
			f.seek(0,0)
			# only read what was not read
			data.append(f.read(bytes))
		# print(str(data[-100:-1]).split("\n"))
		linesFound = data[-1].count(b'\n')
		# print(linesFound)
		size -= linesFound
		bytes -= BUFSIZ
		block -= 1

	#print(data[0].decode())
	return '\n'.join(''.join(data[0].decode()).splitlines()[-window:])

def readAquaOxyLog(filepath):
	#Parses AquaOxyLog o2 only file
	with open(filepath,'r') as f:
		data = f.readlines()[0].split(";")
		oxtime = float(data[0])
		o2 = float(data[1])
	return o2,oxtime

def ReadFirestingFIRMWARE4():
	po2s = {1:0,2:0,3:0,4:0} #Dict for data
	for c in range(1,5):
		#check if file exists
		if os.path.exists(oxypath + str(c)+".aqua"):
			o2,oh2time = readAquaOxyLog(oxypath + str(c)+".aqua")
			if c == 1: oxtime = oh2time
			po2s[c] = o2
			# print(c,o2)

	return po2s[1],po2s[2],po2s[3],po2s[4],oxtime


ReadFirestingFIRMWARE4()

def ReadFiresting(fn):
	with open(fn,'rb') as f:
		ans =  tail(f)

	n = 0

	try:
		pO2_1 = ans.split("\t")[4+n]
		pO2_2 = ans.split("\t")[5+n]
		pO2_3 = ans.split("\t")[6+n]
		pO2_4 = ans.split("\t")[7+n]

		oxtime = ans.split("\t")[1]
	except IndexError:
		print("read error")
		pO2_1 = -4
		pO2_2= -4
		pO2_3= -4
		pO2_4= -4
		oxtime=1

	return pO2_1.replace(",","."),pO2_2.replace(",","."),pO2_3.replace(",","."),pO2_4.replace(",","."),oxtime.replace(",",".")

def ReadFirestingOld(fn):
	with open(fn,'rb') as f:
		ans =  tail(f)

	n = -1
	try:
		pO2_1 = ans.split("\t")[4+n]
		pO2_2 = ans.split("\t")[5+n]
		pO2_3 = ans.split("\t")[6+n]
		pO2_4 = ans.split("\t")[7+n]

		oxtime = ans.split("\t")[1+n]
	except IndexError:
		print("read error")
		pO2_1 = -4
		pO2_2= -4
		pO2_3= -4
		pO2_4= -4


	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime

def ReadFibox3_1ch(fn):
	with open(fn,'rb') as f:
		ans =  tail(f)
	n= -1
	try:
		pO2_1 = ans.split(";")[3].split(" ")[-1]
		oxtime = ans.split(";")[2].split(" ")[-1]
		oxclock = ans.split(";")[1].split(" ")[-1]

	except IndexError:
		pO2_1 = -9999
		oxtime = -9999
		oxclock = "00:00:00"

	return pO2_1, oxtime,oxclock


def ReadPresens4(fn):
	PO2 = []
	for ch in range(1,5):

		fnr = fn + "-ch" +str(ch)+".txt"

		with open(fnr,'rb') as f:
			ans =  tail(f)

		PO2.append(ans.split(";")[3])

	pO2_1 = PO2[0].replace(",",".")
	pO2_2 = PO2[1].replace(",",".")
	pO2_3 = PO2[2].replace(",",".")
	pO2_4 = PO2[3].replace(",",".")
	oxtime = ans.split(";")[1]

	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime



def SensorMess():
	#Keeps track of what sensor is used
	sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave  = filehandling.GetExperimentInfo()

	Firesting = False
	Presens4 = False
	Fibox3 = False
	FNFiresting = "--"
	FNFibox = "--"
	fnslave = mainpath + "oxygen" + os.sep + "firestingSlave.txt"

	if sensor =="2":
		Firesting = False
		Presens4 = False
		Fibox3 = True
		FNFibox =  mainpath + "oxygen" + os.sep + "fibox3.txt"

	elif sensor =="1":
		Firesting = True
		Presens4 = False
		Fibox3 = False
		FNFiresting = mainpath + "oxygen" + os.sep + "firesting.txt"
	elif sensor =="0":
		Firesting = True
		Presens4 = False
		Fibox3 = False
		FNFiresting = mainpath + "oxygen" + os.sep + "firestingnew.txt"


	return Firesting, Presens4, Fibox3, FNFiresting, FNFibox, fnslave

def uniformoxygen():
	Firesting, Presens4, Fibox3, FNFiresting, FNFibox, fnslave = SensorMess()

	if Firesting:
		if "new" in FNFiresting:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime = ReadFirestingFIRMWARE4()
		else:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime = ReadFiresting(FNFiresting)

	if Fibox3:
		pO2_1,oxclock,oxtime = ReadFibox3_1ch(FNFibox)
		pO2_2,pO2_3,pO2_4 = ["-","-","-"]
		pO2_1 = pO2_1.replace(",",".")


	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime

#uniformoxygen()
