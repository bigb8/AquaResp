from ctypes import WinDLL,c_long,c_int,byref
import os,filehandling
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
temppath = mainpath + "temp" + os.sep

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





	
def ReadFiresting(fn):
	with open(fn,'rb') as f:
		ans =  tail(f)
		
	n = 0
	
	# print(ans)
	# pO2_1 = ans.split('\t')[4+n]
	# pO2_2 = ans.split("\t")[5+n]
	# pO2_3 = ans.split("\t")[6+n]
	# pO2_4 = ans.split("\t")[7+n]

	# oxtime = ans.split("\t")[1]
	
	
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
	# print(pO2_1,pO2_2,pO2_3,pO2_4,oxtime)
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime
	
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
	
	if sensor =="4":
		Firesting = False
		Presens4 = False
		Fibox3 = True
		FNFibox =  mainpath + "oxygen" + os.sep + "fibox3.txt"
		
	elif sensor =="0":
		Firesting = True
		Presens4 = False
		Fibox3 = False
		FNFiresting = mainpath + "oxygen" + os.sep + "firesting.txt"
		
		
		
	return Firesting, Presens4, Fibox3, FNFiresting, FNFibox, fnslave			

def uniformoxygen():
	Firesting, Presens4, Fibox3, FNFiresting, FNFibox, fnslave = SensorMess()

	if Firesting:
		pO2_1,pO2_2,pO2_3,pO2_4,oxtime = ReadFiresting(FNFiresting)

	if Fibox3:
		pO2_1,oxclock,oxtime = ReadFibox3_1ch(FNFibox)
		pO2_2,pO2_3,pO2_4 = ["-","-","-"]
		pO2_1 = pO2_1.replace(",",".")
	
	
	return pO2_1,pO2_2,pO2_3,pO2_4,oxtime	
	
#uniformoxygen()
	




