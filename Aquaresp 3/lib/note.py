#TODO


import wx,os,filehandling,time,datetime
mainpath = os.path.dirname(os.path.realpath(__file__)).split("lib")[0]
temppath = mainpath + os.sep +"temp" + os.sep

class notetaker ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AquaNote: Experiment notetaker", pos = wx.DefaultPosition, size = wx.Size( 550,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Update time stamp", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		bSizer4.Add( self.m_button26, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.timeis = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.timeis.Wrap( -1 )
		bSizer4.Add( self.timeis, 0, wx.ALL, 5 )
		
		self.notefield = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.notefield, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.saver = wx.Button( self, wx.ID_ANY, u"Save this note", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		bSizer4.Add( self.saver, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button25 = wx.Button( self, wx.ID_ANY, u"See all notes", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer4.Add( self.m_button25, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button26.Bind( wx.EVT_BUTTON, self.newnote )
		self.saver.Bind( wx.EVT_BUTTON, self.savetofile )
		self.m_button25.Bind( wx.EVT_BUTTON, self.opennotepad )
		
		
		with open(temppath + "timestampstart.txt",'r') as f:
			UNIXtimestart = f.readlines()[0].split(":")[1].split(";")[0]
		self.timeis.SetLabel("timestamp start experiment: " + str(UNIXtimestart))
		self.Show(True)
		
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def savetofile( self, event ):

		pf, slopefolder, expfolder = filehandling.presentfolderFunc()
		
		#Get time stamp
		timestampis = int(time.time())
		humane_time = datetime.datetime.fromtimestamp( int(timestampis)).strftime('%Y-%m-%d %H:%M:%S')
		thenote = self.notefield.GetValue()
		
		try:	
			#Save notefield
			with open(pf + "notes.txt", "a") as f:
				f.write("["+str(humane_time)+";"+str(timestampis)+"]; "+ thenote+ ";\n")
			#Clear notefield
			
			self.notefield.SetValue("")
		except UnicodeEncodeError:
			self.notefield.SetValue("UNICODE CHARACTERS ONLY - ENGLISH LETTERS ----- The following note is not saved: " + thenote)
		# self.timeis.SetLabel("AquaNote, timestamp: 450")
	
	def newnote( self, event ):
	
		timestampis = int(time.time())

		self.timeis.SetLabel("AquaNote, updated timestamp: " + str(timestampis))
		
	def opennotepad( self, event ):
		pf, slopefolder, expfolder = filehandling.presentfolderFunc()
		osCommandString = "notepad.exe "+ pf + "notes.txt"
		# osCommandString = temppath + "notes.txt"
		os.system(osCommandString)
		# os.startfile(osCommandString)

app = wx.App()
notetaker(None)
app.MainLoop()