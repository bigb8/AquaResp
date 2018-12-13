##### PYTHON LIBRARIES ###############

import os,sys

##### EXTERNAL LIBRARIES ###############

import numpy as np

from bokeh.plotting import figure, output_file, show,save
from bokeh.models import BoxSelectTool,ResetTool,WheelZoomTool,HoverTool,CrosshairTool
from bokeh.core.properties import value
from bokeh.io import show, output_file

########### AQUARESP LIBRARIES ###############

import filehandling

########### INIT ###############
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
oxygenpath = mainpath + os.sep +"oxygen" + os.sep
temppath = mainpath + os.sep +"temp" + os.sep
fn = oxygenpath + "firesting.txt"
lib_p = mainpath  + os.sep + "lib" + os.sep
myp = os.path.dirname(sys.argv[0]) + os.sep


############### MO2 vs TIME #######################


for resp in range(1,filehandling.GetNumResp()+1):
	# print(resp)

	# prepare data
	mo2,po2,r2,timeh,num = filehandling.GetsummaryData(resp)
	inuse, volume, animalmass = filehandling.readrespirometerinfo(resp)
	
	
	x = np.array(timeh)
	y = np.array(mo2)
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "MO2_" +str(resp)+ ".html",mode="inline")
	# create a new plot with a title and axis labels
	p = figure(title="Oxygen Consumption: Mass-Specific ", x_axis_label='Time [h]', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(np.array(y).min() -20, np.array(y).max() +20))
	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	# p.scatter(x, y, legend="Resp 1", radius=.2,fill_color=(0,250,0), fill_alpha=0.6,line_color=(0,0,0))
	p.scatter(x, y, legend="Resp 1", radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
	save(p)
	
	x = np.array(timeh)
	y = np.array(mo2)*float(animalmass)
	# y=y
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "MO2_ABS_" +str(resp)+ ".html",mode="inline")
	# create a new plot with a title and axis labels
	p = figure(title="Oxygen Consumption: Absolute ", x_axis_label='Time [h]', y_axis_label='MO2 [mgO2 / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(np.array(y).min(), np.array(y).max()))
	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	# p.scatter(x, y, legend="Resp 1", radius=.2,fill_color=(0,250,0), fill_alpha=0.6,line_color=(0,0,0))
	p.scatter(x, y, legend="Resp 1", radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
	save(p)


	
# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Mass-Specific ", x_axis_label='Time [h]', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(np.array(y).min() -20, np.array(y).max() +20))	
for resp in range(1,filehandling.GetNumResp()+1):
	# print(resp)
	
	# prepare data
	mo2,po2,r2,timeh,num = filehandling.GetsummaryData(resp)

	x = np.array(timeh)
	y = np.array(mo2)
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "MO2_all.html",mode="inline")

	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	p.scatter(x, y, legend="Resp " + str(resp), radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
save(p)


# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Absolute ", x_axis_label='Time [h]', y_axis_label='MO2 [mgO2 / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(-2 , np.array(y).max() +.5))	
for resp in range(1,filehandling.GetNumResp()+1):
	# print(resp)
	
	# prepare data
	mo2,po2,r2,timeh,num = filehandling.GetsummaryData(resp)
	inuse, volume, animalmass = filehandling.readrespirometerinfo(resp)
	
	
	x = np.array(timeh)
	y = np.array(mo2)*float(animalmass)
	
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "MO2_ABS_all.html",mode="inline")

	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	p.scatter(x, y, legend="Resp " + str(resp), radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
save(p)

print("MO2 time plots updated")
	

############### MO2 vs Po2 #######################	
#init
mo2,po2,r2,timeh,num = filehandling.GetsummaryData(1)

x = np.array(po2)
y = np.array(mo2)	



	# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Mass-Specific ", x_axis_label='PO2 [%]', y_axis_label='MO2 [mgO2 / kg / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(np.array(y).min() -.5, np.array(y).max() +20))	
for resp in range(1,filehandling.GetNumResp()+1):
	# print(resp)
	
	# prepare data
	mo2,po2,r2,timeh,num = filehandling.GetsummaryData(resp)

	x = np.array(po2)
	y = np.array(mo2)
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "MO2_PO2.html",mode="inline")

	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	p.scatter(x, y, legend="Resp " + str(resp), radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
save(p)




p = figure(title="Oxygen Consumption: Absolute ", x_axis_label='PO2 [%]', y_axis_label='MO2 [mgO2 / hr]',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(np.array(y).min()-.5 , np.array(y).max()+.5))	
for resp in range(1,filehandling.GetNumResp()+1):
	# print(resp)
	
	# prepare data
	mo2,po2,r2,timeh,num = filehandling.GetsummaryData(resp)

	x = np.array(po2)
	# y = np.array(mo2)
	
	inuse, volume, animalmass = filehandling.readrespirometerinfo(resp)
	
	
	# x = np.array(timeh)
	y = np.array(mo2)*float(animalmass)
	
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "MO2_ABS_PO2.html",mode="inline")

	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	p.scatter(x, y, legend="Resp " + str(resp), radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
save(p)
print("MO2 PO2 plots updated")	
	


############### RSQ vs t #######################	
#init
mo2,po2,r2,timeh,num = filehandling.GetsummaryData(1)

x = np.array(timeh)
y = np.array(r2)	



	# create a new plot with a title and axis labels
p = figure(title="Oxygen Consumption: Mass-Specific ", x_axis_label='Hours', y_axis_label='R-squared.',tools="box_zoom,wheel_zoom,save,hover,reset,crosshair,",tooltips="@y",x_range=(0, np.array(x).max() +5), y_range=(0, 1))	
for resp in range(1,filehandling.GetNumResp()+1):
	# print(resp)
	

	# prepare data
	mo2,po2,r2,timeh,num = filehandling.GetsummaryData(resp)

	x = np.array(timeh)
	y = np.array(r2)
	color = [(255,0,0),(0,255,0),(0,0,255),(125,255,0)]
	# output to static HTML file
	output_file(myp + "R2.html",mode="inline")

	p.toolbar.active_scroll = p.select_one(WheelZoomTool) 
	p.scatter(x, y, legend="Resp " + str(resp), radius=.2,fill_color=color[resp-1], fill_alpha=0.6,line_color=(0,0,0))
	p.line(x, y, alpha=0.6,line_color=(0,0,0))
	# show the results
save(p)




print("RSQ Plots updated")
	


# p.toolbar.active_inspect = [HoverTool, CrosshairTool]
# p.toolbar.active_inspect =  CrosshairTool
# p.toolbar.active_drag = WheelZoomTool()
# p.add_tools(LassoSelectTool())
# p.add_tools(WheelZoomTool())
# p.add_tools(ResetTool()())
# add a line renderer with legend and line thickness
# output_file(myp + "MO2.html")
# output_file(myp + "MO2PO2.html")
# output_file(myp + "R2.html")
