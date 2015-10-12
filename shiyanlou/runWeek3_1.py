# -*- coding: utf8 -*-
__author__ = 'zr'

from class_cmdManager import CmdManager
from class_courseManager import courseManager
from class_course import course
import sys
sys.path.append('D:\\0tmpper\GitHub\python_learn\shiyanlou')
print "2正在加载控制程序"
cm=courseManager()
print "3正在加载界面控制程序"
cmd_man=CmdManager(cm)