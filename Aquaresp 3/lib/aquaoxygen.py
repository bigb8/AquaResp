import numpy as np
from math import exp,log
#Calculates oxygen solubility


def oxygensolubility(temp,salinity):
	c1 = -7.424
	c2 = 4417
	c3 = -2.927
	c4 = 0.04238
	c5 = -0.1288
	c6 = 53.44
	c7 = -0.04442
	c8 = 0.0007145
	c9 = 273.16
	
	oxysolmmhg = exp((c1+(c2/(temp+c9))+(c3*log(temp+c9))+(c4*(temp+c9)))-((salinity-0.03)/1.805)*((c5+(c6/(c9+temp))+(c7*log(c9+temp))+(c8*(c9+temp)))))/22.414*32/760*1000
	oxysolkpa = (oxysolmmhg*760 ) / 101.3
	
	return oxysolmmhg,oxysolkpa
	
	
def partialpressureoxygen(temp, patm, type):
	#Calculates oxygen partial pressure on basis of 
	#temperature
	#atmospheric pressure
	

	if type == "kpa": ## Handles athmospheric pressure and units
		pa = (patm*760)/101.3
		
	elif type =="mmhg":
		pa = patm
		
	else:
		print( "Not Supported unit")
		
	c1= 273.16 
	c2=18.19730 
	c3=373.16 
	c4=3.1813*0.0000001	
	c5=26.12050 
	c6=1.8726*0.01
	c7=8.03945 
	c8 =5.02802 

	pO2max = (pa-exp(c2*(1-(c3/(temp+c1)))+(c4*(1-exp(c5*(1-(temp+c1)/c3))))-(c6*(1-exp(c7*(1-(c3/(temp+c1))))))+(c8*log((c3/(temp+c1)))))*pa)*0.2094
	pO2maxkpa = pO2max/760 * 101.3
	return pO2max, pO2maxkpa
	
def beta1atm(temperature, salinity):

	oxysolmmhg,oxysolkpa = oxygensolubility(temperature,salinity)
	pO2maxmmhg, pO2maxkpa = partialpressureoxygen(temperature, 760, "mmhg")
	# print pO2maxmmhg, oxysolmmhg,oxysolmmhg*pO2maxmmhg*.001
	return oxysolmmhg*pO2maxmmhg*.001
	
# beta1atm(10, 30)
	
	
	