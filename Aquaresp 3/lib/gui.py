import wx,os,sys
import datetime,time
import aquaoxygen
import filehandling
# import Flushy
import aquarespdevice as aqdev
# import main
from subprocess import Popen,run

myp = os.path.dirname(sys.argv[0])
main_p = myp.split("lib")[0]
temp_p = main_p + "temp"
lib_p = main_p + "lib"
print("Active path: ", myp)

def instrumentoptions():
	experimenttypeChoices = ["Standard SMR (Flush -> Wait -> Measure)","MMR and then SMR (Wait -> Measure -> Flush)", "delta pO2 flush","Closed respirometry - for teaching"]
	# experimenttypeChoices = ["Standard SMR (Flush -> Wait -> Measure)","MMR and then SMR (Wait -> Measure -> Flush)", "delta pO2 flush","Adaptive respirometry","Closed respirometry - for teaching"]
	o2sensortypeChoices = ["Pyroscience Firesting 4 channel", "Presens Fibox 3"]
	# o2sensortypeChoices = ["Pyroscience Firesting 4 channel", "Pyroscience Firesting 3 channel","Pyroscience Firesting 2 channel","Pyroscience Firesting 1 channel","Presens Fibox 3"]
	typeADChoices = ["Cleware 1","Cleware 4","Measurement Computing 1208LS"]
	return experimenttypeChoices,o2sensortypeChoices,typeADChoices
		
class EandE ( wx.Frame ):
	

		
		
	
	def __init__( self, parent ):
	
		experimenttypeChoices,o2sensortypeChoices,typeADChoices = instrumentoptions()
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Equipment and Experiment", pos = wx.DefaultPosition, size = wx.Size( 580,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 580,350 ), wx.Size( 580,350 ) )
		
		gSizer5 = wx.GridSizer( 2, 0, 0 )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Oxygen Sensor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		gSizer5.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		# o2sensortypeChoices = []
		self.o2sensortype = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, o2sensortypeChoices, 0 )
		self.o2sensortype.SetSelection( 0 )
		gSizer5.Add( self.o2sensortype, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText64 = wx.StaticText( self, wx.ID_ANY, u"Digital Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		gSizer5.Add( self.m_staticText64, 0, wx.ALL, 5 )
		
		# typeADChoices = []
		self.typeAD = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, typeADChoices, 0 )
		self.typeAD.SetSelection( 0 )
		gSizer5.Add( self.typeAD, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.portoutlab = wx.StaticText( self, wx.ID_ANY, u"Digital port ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.portoutlab.Wrap( -1 )
		gSizer5.Add( self.portoutlab, 0, wx.ALL, 5 )
		
		self.portout = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.portout, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Test flush", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		gSizer5.Add( self.m_staticText66, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Toggle flush pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Experiment type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		gSizer5.Add( self.m_staticText65, 0, wx.ALL, 5 )
		
		# experimenttypeChoices = []
		self.experimenttype = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, experimenttypeChoices, 0 )
		self.experimenttype.SetSelection( 0 )
		gSizer5.Add( self.experimenttype, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"Flush, Wait, Measure (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )
		gSizer5.Add( self.m_staticText68, 0, wx.ALL, 5 )
		
		gSizer9 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.flush = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		gSizer9.Add( self.flush, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.wait = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		gSizer9.Add( self.wait, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.measure = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		gSizer9.Add( self.measure, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		gSizer5.Add( self.m_staticText69, 0, wx.ALL, 5 )
		
		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )
		gSizer5.Add( self.m_staticText70, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		gSizer5.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.m_staticText72 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )
		gSizer5.Add( self.m_staticText72, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetBackgroundColour( wx.Colour( 185, 255, 193 ) )
		
		gSizer5.Add( self.m_button7, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		self.SetSizer( gSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
		#Load data to inputs
		self.InitOldSettingsFromFile()
		
		# Connect Events
		self.typeAD.Bind( wx.EVT_CHOICE, self.disabledigport )
		self.m_button5.Bind( wx.EVT_BUTTON, self.StartStopFlush )
		self.m_button7.Bind( wx.EVT_BUTTON, self.SaveSettings )
		
		self.Show(True)
		
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def disabledigport( self, event ):
		if self.typeAD.GetSelection() > 1:
			self.portout.Enable( False )
			self.portoutlab.Enable( False )
		else:
			self.portout.Enable( True )
			self.portoutlab.Enable( True )
			
	import subprocess
	global tog
	tog	= 1
	def StartStopFlush( self, event ):
		# interface,deviceNo =  Flushy.GiveDeviceInterface()	
		# devno = 0
		# ch1 = 16
		# Flushy.FlipFlop(interface,devno,ch1)
		global tog
		tog = 1- tog
		#Popen(["py","-3","-i", lib_p + os.sep + "Pump.py",str(tog),"0","1"])
		Popen(["py","-3", lib_p + os.sep + "Pump.py",str(tog),"0","1"])
	

	
	def InitOldSettingsFromFile(self):
	#Populates fields in GUI
	
		experimenttypeChoices,o2sensortypeChoices,typeADChoices = instrumentoptions()
		
		
		guidict = {"O2 Sensor":self.o2sensortype, "AD":self.typeAD,"Experiment type":self.experimenttype,"----":None,"Flush":self.flush,"wait":self.wait,"measure":self.measure}

		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		temppath = mainpath + os.sep +"temp" + os.sep
		
		
		with open(temppath + "experiment.txt", 'r') as f:
			for i,l in enumerate(f.readlines()):
				try:
					guidict[l.split(":")[0]].SetSelection(int(l.split(":")[1].split(";")[0]))
				except TypeError:
					guidict[l.split(":")[0]].SetValue(l.split(":")[1].split(";")[0])
				except KeyError: pass
				
		#Disables port out (Yes - hardcoded)
		if self.typeAD.GetSelection() > 1:
			self.portout.Enable( False )
			self.portoutlab.Enable( False )
		else:
			self.portout.Enable( True )
			self.portoutlab.Enable( True )
			

	
	def SaveSettings( self, event ):
	#Saves fields from GUI
		
		experimenttypeChoices,o2sensortypeChoices,typeADChoices = instrumentoptions()
		
		

		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		temppath = mainpath + os.sep +"temp" + os.sep
		with open(temppath + "experiment.txt", 'w') as f:
			f.write("O2 Sensor:"+str(self.o2sensortype.GetSelection())+";"+ o2sensortypeChoices[self.o2sensortype.GetSelection()]+";\n")
			f.write("AD:"+str(self.typeAD.GetSelection())+";"+ typeADChoices[self.typeAD.GetSelection()]+";\n")
			f.write("Experiment type:"+str(self.experimenttype.GetSelection())+";"+ experimenttypeChoices[self.experimenttype.GetSelection()]+";\n")
			# f.write("----;;\n")
			f.write("Flush:"+str(self.flush.GetValue())+";;\n")
			f.write("wait:"+str(self.wait.GetValue())+";;\n")
			f.write("measure:"+str(self.measure.GetValue())+";;\n")
			

			
		self.Close()
	


class animalssss ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Animal Settings", pos = wx.DefaultPosition, size = wx.Size( 676,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 675,480 ), wx.DefaultSize )
		
		gSizer4 = wx.GridSizer( 4, 0, 0 )
		
		gSizer4.SetMinSize( wx.Size( -1,25 ) ) 
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Respirometers in use (Click to activate)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		gSizer4.Add( self.m_staticText40, 1, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		gSizer4.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		gSizer4.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		gSizer4.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Respirometer 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True) 
		gSizer4.Add( self.m_checkBox1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Respirometer 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_checkBox2, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"Respirometer 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_checkBox3, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"Respirometer 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_checkBox4, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Volumes (L)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		gSizer4.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		gSizer4.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		gSizer4.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		gSizer4.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.vresp1 = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.vresp1, 0, wx.ALL, 5 )
		
		self.vresp2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.vresp2, 0, wx.ALL, 5 )
		
		self.vresp3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.vresp3, 0, wx.ALL, 5 )
		
		self.vresp4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.vresp4, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Animal mass (kg)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		gSizer4.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer4.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		gSizer4.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		gSizer4.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		self.mresp1 = wx.TextCtrl( self, wx.ID_ANY, u"0.25", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.mresp1, 0, wx.ALL, 5 )
		
		self.mresp2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.mresp2, 0, wx.ALL, 5 )
		
		self.mresp3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.mresp3, 0, wx.ALL, 5 )
		
		self.mresp4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.mresp4, 0, wx.ALL, 5 )
		
		self.TemperatureLab = wx.StaticText( self, wx.ID_ANY, u"Temperature (*C)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TemperatureLab.Wrap( -1 )
		gSizer4.Add( self.TemperatureLab, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.SalinityLab = wx.StaticText( self, wx.ID_ANY, u"Salinity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SalinityLab.Wrap( -1 )
		gSizer4.Add( self.SalinityLab, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.asdfasdf = wx.StaticText( self, wx.ID_ANY, u"Oxygen Solubility ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asdfasdf.Wrap( -1 )
		gSizer4.Add( self.asdfasdf, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		gSizer4.Add( self.m_staticText58, 0, wx.ALL, 5 )
		
		self.Temperature = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Temperature, 0, wx.ALL, 5 )
		
		self.Salinity = wx.TextCtrl( self, wx.ID_ANY, u"32", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.Salinity, 0, wx.ALL, 5 )
		
		self.OxySol = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OxySol.Enable( False )
		
		gSizer4.Add( self.OxySol, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"mg O2 / L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		gSizer4.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		gSizer4.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gSizer4.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		gSizer4.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetMinSize( wx.Size( -1,100 ) )
		self.m_button4.SetBackgroundColour( wx.Colour( 142, 244, 148 ) )
		
		gSizer4.Add( self.m_button4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
		
		#Load data to inputs
		self.InitOldSettingsFromFile()
		# Connect Events
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.resp1act )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.resp2act )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.resp3act )
		self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.resp4act )
		self.Temperature.Bind( wx.EVT_TEXT, self.CalcBeta )
		self.Salinity.Bind( wx.EVT_TEXT, self.CalcBeta )
		self.m_button4.Bind( wx.EVT_BUTTON, self.SaveNQuit )
	
		
	
		
		self.Show(True)
	
	def __del__( self ):
		pass
	def InitOldSettingsFromFile(self):
	#Populates fields in GUI
		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		temppath = mainpath + os.sep +"temp" + os.sep
		respdict = {1: self.m_checkBox1,2:self.m_checkBox2,3:self.m_checkBox3,4:self.m_checkBox4}
		voldict = {1: self.vresp1,2:self.vresp2,3:self.vresp3,4:self.vresp4}
		massdict = {1: self.mresp1,2:self.mresp2,3:self.mresp3,4:self.mresp4}
		waterdict = {1: self.Temperature,2:self.Salinity,3:self.OxySol}
		guidict = {"In use":respdict, "volume":voldict,"animal mass":massdict}
		
		for i in range(1,5):
			try:
				with open(temppath + "respirometer_"+str(i)+".txt", 'r') as f:
					for ii,l in enumerate(f.readlines()):
						if ii == 0:
							if l.split(":")[1].split(";")[0] =="y":
								respdict[i].SetValue(True)
							else:
								respdict[i].SetValue(False)
								massdict[i].Enable( False )
								voldict[i].Enable( False ) 
						else:		
							guidict[l.split(":")[0]][i].SetValue(l.split(":")[1].split(";")[0])
			except IOError:
				respdict[i].SetValue(False) 
				massdict[i].Enable( False )
				voldict[i].Enable( False ) 
			
			
		with open(temppath + "water.txt", 'r') as f:
			for ii,l in enumerate(f.readlines()):
				waterdict[ii+1].SetValue(l.split(":")[1].split(";")[0])

				
	

	def resp1act( self, event ):
		if self.m_checkBox1.GetValue() == False:
			self.vresp1.Enable( False )
			self.mresp1.Enable( False )
			
			#Disable respirometer 2 option
			self.m_checkBox2.Enable( False )
			self.m_checkBox2.SetValue(False)
			self.vresp2.Enable( False )
			self.mresp2.Enable( False )
			#Disable respirometer 3 option
			self.m_checkBox3.Enable( False )
			self.m_checkBox3.SetValue(False)
			self.vresp3.Enable( False )
			self.mresp3.Enable( False )

			#Disable respirometer 4 option
			self.m_checkBox4.Enable( False )
			self.m_checkBox4.SetValue(False)
			self.vresp4.Enable( False )
			self.mresp4.Enable( False )

			
		else:
			self.vresp1.Enable( True )
			self.mresp1.Enable( True)
			
			#Enable respirometer 2 option
			self.m_checkBox2.Enable( True )
			#Enable respirometer 3 option
			self.m_checkBox3.Enable( True )
			#Enable respirometer 4 option
			self.m_checkBox4.Enable( True )
			
			
			
			
			
	
	def resp2act( self, event ):
		# if not self.resp1act:
	
		if self.m_checkBox2.GetValue() == False:
			self.vresp2.Enable( False )
			self.mresp2.Enable( False )
		else:
			self.vresp2.Enable( True )
			self.mresp2.Enable( True)
	
		# event.Skip()
	
	def resp3act( self, event ):
		if self.m_checkBox3.GetValue() == False:
			self.vresp3.Enable( False )
			self.mresp3.Enable( False )
		else:
			self.vresp3.Enable( True )
			self.mresp3.Enable( True)
	
	def resp4act( self, event ):
		if self.m_checkBox4.GetValue() == False:
			self.vresp4.Enable( False )
			self.mresp4.Enable( False )
		else:
			self.vresp4.Enable( True )
			self.mresp4.Enable( True)
	
	def CalcBeta( self, event ):
		t = self.Temperature.GetValue()
		s = self.Salinity.GetValue()
		try:
			beta = aquaoxygen.beta1atm(float(t), float(s))
			self.OxySol.SetValue(str(beta))
		except ValueError:
			self.OxySol.SetValue(str("-"))
		
		
	
	def SaveNQuit( self, event ):
		# import os
		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		temppath = mainpath + os.sep +"temp" + os.sep
		#Save all values
		
		#Check boxes
		respdict = {1: self.m_checkBox1,2:self.m_checkBox2,3:self.m_checkBox3,4:self.m_checkBox4}
		voldict = {1: self.vresp1,2:self.vresp2,3:self.vresp3,4:self.vresp4}
		massdict = {1: self.mresp1,2:self.mresp2,3:self.mresp3,4:self.mresp4}
		
		
		
		numresp = 0 # Number of active respirometers
		isactive = []
		notactive = []
		for i in respdict:
			if respdict[i].GetValue() == True:
				numresp+=1
				isactive.append(i)
			else:
				notactive.append(i)
				
		# print(isactive)
		for i in isactive:
			with open(temppath + "respirometer_" + str(i) + ".txt", 'w') as f:
				f.write("In use:y;\n")
				f.write("volume:"+ str(voldict[i].GetValue()) +";\n")
				f.write("animal mass:"+ str(massdict[i].GetValue()) +";\n")
				# f.write("a\n")
				
		for i in notactive:
			with open(temppath + "respirometer_" + str(i) + ".txt", 'w') as f:
				f.write("In use:n;\n")
				f.write("volume:"+ str(voldict[i].GetValue()) +";\n")
				f.write("animal mass:"+ str(massdict[i].GetValue()) +";\n")
			
		with open(temppath + "water.txt", 'w') as f:
			f.write("Temperature:"+str(self.Temperature.GetValue())+";\n")
			f.write("Salinity:"+str(self.Salinity.GetValue())+";\n")
			f.write("Oxygen Solubility:"+str(self.OxySol.GetValue())+";\n")
		
		with open(temppath + "numresp.txt", 'w') as f:
			f.write(str(numresp))
		
		# self.InitMainFrame()
		
		self.Close()
		# event.Skip()
	

class RunningExperiment ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Experiment Running", pos = wx.DefaultPosition, size = wx.Size( 489,354 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 2, 0, 0 )
		
		gSizer6.SetMinSize( wx.Size( -1,30 ) ) 
		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, u"Current period", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		gSizer6.Add( self.m_staticText73, 0, wx.ALL, 5 )
		
		self.currentperiod = wx.StaticText( self, wx.ID_ANY, u"not started", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.currentperiod.Wrap( -1 )

		gSizer6.Add( self.currentperiod, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"Progression", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )
		gSizer6.Add( self.m_staticText76, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		self.PeriodStatus = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.PeriodStatus.SetValue( 0 ) 
		self.PeriodStatus.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3.Add( self.PeriodStatus, 1, wx.ALL|wx.EXPAND, 5 )
			
		fgSizer2 = wx.FlexGridSizer( 0, 10, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
			
		bSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer22 = wx.FlexGridSizer( 0, 10, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.R2lab1 = wx.StaticText( self, wx.ID_ANY, u"pO2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.R2lab1.Wrap( -1 )
		fgSizer22.Add( self.R2lab1, 0, wx.ALL, 5 )
		
		self.r211 = wx.StaticText( self, wx.ID_ANY, u"--------", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.r211.Wrap( -1 )
		fgSizer22.Add( self.r211, 0, wx.ALL, 5 )
		
		self.r221 = wx.StaticText( self, wx.ID_ANY, u"--------", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.r221.Wrap( -1 )
		fgSizer22.Add( self.r221, 0, wx.ALL, 5 )
		
		self.r231 = wx.StaticText( self, wx.ID_ANY, u"--------", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.r231.Wrap( -1 )
		fgSizer22.Add( self.r231, 0, wx.ALL, 5 )
		
		self.r241 = wx.StaticText( self, wx.ID_ANY, u"--------", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.r241.Wrap( -1 )
		fgSizer22.Add( self.r241, 0, wx.ALL, 5 )
		
		self.m_staticText962 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText962.Wrap( -1 )
		fgSizer22.Add( self.m_staticText962, 0, wx.ALL, 5 )
		
		self.m_staticText972 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText972.Wrap( -1 )
		fgSizer22.Add( self.m_staticText972, 0, wx.ALL, 5 )
		
		self.m_staticText982 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText982.Wrap( -1 )
		fgSizer22.Add( self.m_staticText982, 0, wx.ALL, 5 )
		
		self.m_staticText992 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText992.Wrap( -1 )
		fgSizer22.Add( self.m_staticText992, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer22, 1, wx.EXPAND, 5 )
		
		gSizer10 = wx.GridSizer( 1, 4, 0, 0 )
		
		self.m_button132 = wx.Button( self, wx.ID_ANY, u"Stop (2x click)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button132.SetBackgroundColour( wx.Colour( 247, 89, 89 ) )
		
		gSizer10.Add( self.m_button132, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Exp. control", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.Enable( False )
		
		gSizer10.Add( self.m_button21, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.graphs = wx.Button( self, wx.ID_ANY, u"Graphs", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.graphs, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.writenote = wx.Button( self, wx.ID_ANY, u"Write a note", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.writenote.SetDefault() 
		gSizer10.Add( self.writenote, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button132.Bind( wx.EVT_LEFT_DCLICK, self.STOOOOP )
		self.graphs.Bind( wx.EVT_BUTTON, self.graphss )
		self.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
		# self.m_button21.Bind( wx.EVT_BUTTON, self.pcrittt )
		self.writenote.Bind( wx.EVT_BUTTON, self.writenotetoexperiment )
		self.Show(True)
		
		# while 1:
			# time.sleep(1)
		self.UpdateGui()
	
	def __del__( self ):
		pass
	
	global forcer
	forcer = 0
	def onKeyPress(self,event):
		global forcer
		if event.GetKeyCode() == 308:
			forcer +=1
			
			if forcer > 3:
				filehandling.FORCEMEASUREMENTEND()
				forcer = 0
		# if wx.ControlDown(self):
			
			# print(event)
			

	def STOOOOP( self, event ):
		print("Stop requested ... ")
		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		temppath = mainpath + os.sep +"temp" + os.sep
		with open(temppath + "runningexperiment.txt",'w') as f:
			f.write(str(0))
				
		#Clean up files
		filehandling.CleanSummaryData()
		
		
		#Start flushing
		Popen(["python", lib_p + os.sep + "Pump.py","1","0","1"])
		print("Goodbye - you can close all windows now")
		self.Close()

		
	def UpdateGui(self):
		# currentperiod
		period = filehandling.TjekPeriod()
		if period =="F": 
			real = "Flushing"
			self.currentperiod.SetForegroundColour("red")
		if period =="W": 
			real = "Wait period"
			self.currentperiod.SetForegroundColour("yellow")
		if period =="M": 
			real = "Measurement"
			self.currentperiod.SetForegroundColour("Green")
		try:
			self.currentperiod.SetLabel(real)
		except:
			pass
		
		# pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = filehandling.GetLastOxygen()
		# mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		try:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = aqdev.uniformoxygen()
		except:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = [0,0,0,0,0]
		
		self.r211.SetLabel(str(pO2_1))
		self.r221.SetLabel(str(pO2_2))
		self.r231.SetLabel(str(pO2_3))
		self.r241.SetLabel(str(pO2_4))
		
		try:
			with open(temp_p + os.sep + "lastmo2.txt", 'r') as ffff:
				mo2ss = ffff.read.lines()[0].split(";")
		except: pass
		
		try:
			self.mo1.SetLabel(str(mo2ss[0]))
		except: pass
		
		try:
			self.mo1.SetLabel(str(mo2ss[1]))
		except: pass
		
		try:
			self.mo1.SetLabel(str(mo2ss[2]))
		except: pass
		
		try:
			self.mo1.SetLabel(str(mo2ss[3]))
		except: pass		

		try:
			with open(temp_p + os.sep + "last2.txt", 'r') as ffff:
				r2ss = ffff.read.lines()[0].split(";")
			
			self.r21.SetLabel(str(r2ss[0]))
			self.r22.SetLabel(str(r2ss[1]))
			self.r23.SetLabel(str(r2ss[2]))
			self.r24.SetLabel(str(r2ss[3]))
		except: pass
					
		
		
		try:
			startperiod, time,timesince = filehandling.GetperiodStart()
			mypercent = 100*timesince / time 
			self.PeriodStatus.SetValue(mypercent)
		except:
			self.PeriodStatus.SetValue(50)
		# self.PeriodStatus.SetFirstGradientColour(wx.Colour(0, 0, 0))
		
		wx.CallLater(int(1000), self.UpdateGui)
		
		
		
		# event.Skip()
			
	def pcrittt( self, event ):
		# subprocess.Popen(["python",os.path.dirname(os.path.realpath(__file__)) + os.sep + "startplot.py"])
		event.Skip()
			
	def graphss( self, event ):
		# Popen(["python",os.path.dirname(os.path.realpath(__file__)) + os.sep + "startplot.py"])
		import webbrowser
		from urllib.request import pathname2url # Python 3.x
		
		url = 'file:{}'.format(pathname2url(os.path.dirname(os.path.realpath(__file__)).split("lib")[0] + os.sep + "plots.html"))	
		webbrowser.open_new_tab(url)

		
	
	def writenotetoexperiment( self, event ):
		Popen(["python",os.path.dirname(os.path.realpath(__file__)) + os.sep + "note.py"])


class MainFrame( wx.Frame ):
	
	def __init__( self, parent ):
		
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AquaResp v.3", pos = wx.DefaultPosition, size = wx.Size( 300,500 ) )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Experiment name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.startbutton = wx.Button( self, wx.ID_ANY, u"Start Experiment", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.startbutton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.startbutton.SetBackgroundColour( wx.Colour( 142, 244, 148 ) )
		
		bSizer1.Add( self.startbutton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.animsett = wx.Button( self, wx.ID_ANY, u"Animal settings", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer1.Add( self.animsett, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.equipset = wx.Button( self, wx.ID_ANY, u"Equipment and experiment settings", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer1.Add( self.equipset, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.times = wx.StaticText( self, wx.ID_ANY, u"Flush, Wait, Measure: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.times.Wrap( -1 )
		bSizer1.Add( self.times, 0, wx.ALL, 5 )
		
		self.ExpTypeLabel = wx.StaticText( self, wx.ID_ANY, u"Standard IMF fixed periods (Flush - > Wait -> Measure)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ExpTypeLabel.Wrap( -1 )
		# self.ExpTypeLabel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.ExpTypeLabel.SetBackgroundColour( wx.Colour( 142, 100, 148 ) )
		
		bSizer1.Add( self.ExpTypeLabel, 0, wx.ALL, 5 )
		
		self.numberanimalslabel = wx.StaticText( self, wx.ID_ANY, u"Number of chambers: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.numberanimalslabel.Wrap( -1 )
		bSizer1.Add( self.numberanimalslabel, 0, wx.ALL, 5 )
		
		self.sensorlabel = wx.StaticText( self, wx.ID_ANY, u"Current sensor: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sensorlabel.Wrap( -1 )
		bSizer1.Add( self.sensorlabel, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Verification of pO2 values: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.ch1label = wx.StaticText( self, wx.ID_ANY, u"Channel 1: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1label.Wrap( -1 )
		bSizer1.Add( self.ch1label, 0, wx.ALL, 5 )
		
		self.ch2label = wx.StaticText( self, wx.ID_ANY, u"Channel 2: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2label.Wrap( -1 )
		bSizer1.Add( self.ch2label, 0, wx.ALL, 5 )
		
		self.ch3label = wx.StaticText( self, wx.ID_ANY, u"Channel 3: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch3label.Wrap( -1 )
		bSizer1.Add( self.ch3label, 0, wx.ALL, 5 )
		
		self.ch4label = wx.StaticText( self, wx.ID_ANY, u"Channel 4: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch4label.Wrap( -1 )
		bSizer1.Add( self.ch4label, 0, wx.ALL, 5 )
		
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
		#Load data to inputs
		self.InitMainFrame()
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.refresh )
		self.startbutton.Bind( wx.EVT_BUTTON, self.StartExp )
		self.animsett.Bind( wx.EVT_BUTTON, self.OpenAnimal )
		self.equipset.Bind( wx.EVT_BUTTON, self.OpenEquiptment )
		self.Show(True)
		
		

	
	def __del__( self ):
		pass
		
	def refresh(self,event):
		self.InitMainFrame()
	def InitMainFrame(self):
		
		#Populates fields in GUI
		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		temppath = mainpath + os.sep +"temp" + os.sep
		with open(temppath + "experiment.txt", 'r') as f:
			for i,l in enumerate(f.readlines()):
				if l.split(":")[0] == "O2 Sensor":
					try:
						self.sensorlabel.SetLabel("Sensor: "+l.split(":")[1].split(";")[1])
					except RuntimeError:
						return
					
				if l.split(":")[0] == "Experiment type":
					self.ExpTypeLabel.SetLabel(l.split(":")[1].split(";")[1])
				
				if l.split(":")[0] == "Flush":
					fl = "Flush: " + l.split(":")[1].split(";")[0] + "s, "

				if l.split(":")[0] == "wait":
					fl = fl + "Wait: " + l.split(":")[1].split(";")[0]+ "s, "
	
				if l.split(":")[0] == "measure":
					fl = fl + "Measure: " + l.split(":")[1].split(";")[0] + "s"
					self.times.SetLabel(fl)
				
		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		
		try:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = aqdev.uniformoxygen()
			
			
		except:
			pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = [0,0,0,0,0]
		
		# pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = aqdev.ReadFiresting(mainpath + os.sep + "oxygen" + os.sep + "firesting.txt")
		# pO2_1,pO2_2,pO2_3,pO2_4,oxtime1 = filehandling.GetLastOxygen()
		# filehandling.ox2file(pO2_1,pO2_2,pO2_3,pO2_4,oxtime1)
		
		self.ch1label.SetLabel("Channel 1: " + str(pO2_1))
		self.ch2label.SetLabel("Channel 2: " + str(pO2_2))
		self.ch3label.SetLabel("Channel 3: " + str(pO2_3))
		self.ch4label.SetLabel("Channel 4: " + str(pO2_4))
		

		
		with open(temppath + "numresp.txt", 'r') as f:
			self.numberanimalslabel.SetLabel("Number of chambers: "+ str(f.readline()))
		
		wx.CallLater(int(2000), self.InitMainFrame)		
		
		
	# Virtual event handlers, overide them in your derived class
	def StartExp( self, event ):
		mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
		lib_p = os.path.dirname(os.path.realpath(__file__)).split("lib")[0] + "lib" + os.sep
		temppath = mainpath + os.sep +"temp" + os.sep
		directory = "results"+os.sep+"Experiment_" + self.m_textCtrl1.GetValue() +" " + str(datetime.datetime.now().strftime("%d %B %Y %I %M%p"))
		
		if not os.path.exists(mainpath + directory):
			os.makedirs(mainpath + directory)
		
		with open(temppath + "presentfolder.txt",'w') as f:
			f.write(mainpath+directory+os.sep)
			
		with open(temppath + "runningexperiment.txt",'w') as f:
			f.write(str(1))
			
		sensor,AD, ExpType, ft,wt,mt,temperature,salinity,o2sol, UNIXtime, Dateime, IsSlave = filehandling.GetExperimentInfo()
		filehandling.datafileinit()
		# print ExpType
		# print self.m_textCtrl1.GetValue()
		RunningExperiment(None)
		Popen(["python", lib_p + os.sep +"main.py ",str(ExpType), str(ft),str(wt),str(mt),str(3),str(60)])
		filehandling.SetTimeStartExperiment()
		
		
		self.Close()
		
	
	def OpenAnimal( self, event ):
		animalssss(None)
		
	
	def OpenEquiptment( self, event ):
		EandE(None)
		
	
app = wx.App()
MainFrame(None)
app.MainLoop()
	
