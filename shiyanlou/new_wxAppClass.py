import wx

class myApp(wx.App):
	def __init__(self):
		wx.App.__init__(self)
	
	def OnInit(self):
		self.frame= wx.Frame(parent=None,title='yzr first class')
		self.bkg=wx.Panel(self.frame)
		self.buttons(self.frame)
		self.texts(self.frame)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

	def buttons(self,frames):
		lb=wx.Button(frames,label='Open',pos=(225,5),size=(80,25))
		sb=wx.Button(frames,label='Save',pos=(315,5),size=(80,25))

	def texts(self,frames):
		fileName=wx.TextCtrl(frames,pos=(5,5),size=(210,25))
		contents=wx.TextCtrl(frames,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
		
app = myApp()

app.MainLoop()