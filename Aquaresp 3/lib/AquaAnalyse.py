import time
import os, sys
import datetime as dtt
import numpy as np
from math import exp,log
from scipy import stats

#AQUARESP LIBS
import aquaoxygen as ao


def sloper(x_time,po2):
##Calculates slope of whatever
	x = x_time
	y = po2
	#Only for positive time in measurement period
	y_samplingcorrected = y[x>0]
	x_samecorr = x[x>0]
	slope, intercept, r_value, p_value, std_err = stats.linregress(x_samecorr,y_samplingcorrected)
	rr,pp = stats.pearsonr(x_samecorr,y_samplingcorrected)
	
	
	return slope, intercept, rr, p_value, std_err,np.mean(y_samplingcorrected),np.median(y_samplingcorrected),np.min(y_samplingcorrected),np.max(y_samplingcorrected)


def mo2maker(slope,temp,salinity,patm,mfish,vresp):
# ##Calculates MO2 on basis of:
# ## slope 
# ## temperature 
# ## salinity
# ## fish size
# ## volume of respirometer
# ## barometric pressue

	pO2max, pO2maxkpa = ao.partialpressureoxygen(temp, patm, "mmhg")
	oxysolmmhg,oxysolkpa = ao.oxygensolubility(temp,salinity)
	
	vreal = vresp - mfish
	rRespFish = float(vreal)/mfish
	
	beta = pO2max * oxysolmmhg / 1000.0  # divide by 1000 to get mg O2 / L
	
	MO2 = -1*(slope/100)*beta*rRespFish*3600.0
	MO2_TOT = -1*(slope/100)*beta*vresp*3600.0
        #only per period change to hour
	#and slope is percentage air. this shouldchangetoo
	return MO2, beta, rRespFish,MO2_TOT

	
	
	
