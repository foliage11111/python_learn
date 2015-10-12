# -*- coding: gbk -*-
import wx
import sys
import sqlite3
from class_courseManager2 import courseManager

class myApp(wx.App):
	def __init__(self):
		wx.App.__init__(self)
		self.cm=courseManager()
	
	def OnInit(self):
		self.frame= wx.Frame(parent=None,title='yzr first class',size=(800,250))
		self.bkg=wx.Panel(self.frame)
		self.buttons(self.bkg)
		self.texts(self.bkg)

		hbox=wx.BoxSizer(wx.VERTICAL)
		hbox.Add(self.fileName,proportion=1,flag=wx.EXPAND)
		hbox.Add(self.b1,proportion=1,flag=wx.LEFT,border=5)
		hbox.Add(self.b2,proportion=1,flag=wx.LEFT,border=5)
		hbox.Add(self.b3,proportion=1,flag=wx.LEFT,border=5)
		hbox.Add(self.b4,proportion=1,flag=wx.LEFT,border=5)
		hbox.Add(self.b5,proportion=1,flag=wx.LEFT,border=5)


		vbox=wx.BoxSizer()
		vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
		vbox.Add(self.contents,proportion=1,flag=wx.EXPAND| wx.LEFT | wx.BOTTOM| wx.RIGHT,border=5)
		self.bkg.SetSizer(vbox)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

	def on_click_buttons1(self,event):
		'显示所有课程'
		str1=''
		for k in self.cm.print_all_course():
			str1=str1+ '课程ID为 '+str(k[0])+' ，课程名字为：'+ str(k[1])+'\n'
		self.contents.Clear()
		self.contents.SetValue(str1)

	def on_click_buttons2(self,event):
		'显示某个id的课程'
		str1=''
		for k in self.cm.print_course_id(self.fileName.GetValue()):
			str1=str1+ '课程ID为 '+str(k[0])+' ，课程名字为：'+ str(k[1])+'\n'
		self.contents.Clear()
		self.contents.SetValue("查询结果："+"\n"+str1)

	def on_click_buttons3(self,event):
		'删除某个课程'
		str1=''
		if self.cm.del_course(self.fileName.GetValue()):
			self.contents.Clear()
			self.contents.SetValue("查询结果："+"\n"+str1)
		else:
			self.contents.Clear()
			self.contents.SetValue('删除失败')

	def on_click_buttons4(self,event):
		'显示最长的课程'
		str1=""
		for i in self.cm.print_longest():
			str1=str1+str(i)
		self.contents.Clear()
		self.contents.SetValue("最长课程名称为："+str1)

	def on_click_buttons5(self,event):
		'新增最长的课程'
		list1= self.fileName.GetValue().split(',')
		print list1
		if len(list1)==4:
			if self.cm.in_cour(list1):
				self.contents.Clear()
				self.contents.SetValue("保存成功")
			else:
				self.contents.Clear()
				self.contents.SetValue("保存失败,请按ID，NAME，DATE，IS_IN_USE格式输入")
		else:
			self.contents.Clear()
			self.contents.SetValue("保存失败,请按ID，NAME，DATE，IS_IN_USE格式输入")


	def buttons(self,frames):
		self.b1=wx.Button(frames,label='获取全部课程')
		self.frame.Bind(wx.EVT_BUTTON,self.on_click_buttons1,self.b1)
		self.b2=wx.Button(frames,label='查询课程')
		self.frame.Bind(wx.EVT_BUTTON,self.on_click_buttons2,self.b2)
		self.b3=wx.Button(frames,label='删除课程')
		self.frame.Bind(wx.EVT_BUTTON,self.on_click_buttons3,self.b3)
		self.b4=wx.Button(frames,label='查询最长课程')
		self.frame.Bind(wx.EVT_BUTTON,self.on_click_buttons4,self.b4)
		self.b5=wx.Button(frames,label='新增课程')
		self.frame.Bind(wx.EVT_BUTTON,self.on_click_buttons5,self.b5)


	def texts(self,frames):
		self.fileName=wx.TextCtrl(frames,pos=(5,5),size=(210,25))
		self.contents=wx.TextCtrl(frames,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)

app = myApp()

app.MainLoop()
