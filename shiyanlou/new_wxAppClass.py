import wx

class myApp(wx.App):
	def __init__(self):
		wx.App.__init__(self)
	
	def OnInit(self):
		self.frame= wx.Frame(parent=None,title='yzr first class')
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True
		
app = myApp()

lb=wx.Button(app.frame,label='Open',pos=(225,5),size=(80,25))
sb=wx.Button(app.frame,label='Save',pos=(315,5),size=(80,25))
fileName=wx.TextCtrl(app.frame,pos=(5,5),size=(210,25))
contents=wx.TextCtrl(app.frame,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
app.MainLoop()