
# -*- coding: utf8 -*-
__author__ = 'zr'

import class_cmdManager
import class_courseManager
import clas_database
import class_course

print "0正在创建数据"
data_con_dict=database_dict()
print "1正在加载数据"
css=course(6,'Python','2015-10-4','yes')
data_con_dict.in_up_course(css)
data_con_dict.in_up_course(course(1,'Linux','2015-10-4','yes'))
data_con_dict.in_up_course(course(2,'HTML','2015-10-4','yes'))
data_con_dict.in_up_course(course(3,'HTML5','2015-10-4','yes'))
data_con_dict.in_up_course(course(4,'NodeJS','2015-10-4','yes'))
data_con_dict.in_up_course(course(5,'Shell','2015-10-4','yes'))
print "2正在加载控制程序"
cm=courseManager()
print "3正在加载界面控制程序"
cmd_man=CmdManager(cm,data_con_dict)