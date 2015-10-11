# -*- coding:utf8 -*-

import class_course
import clas_database
import class_courseManager

class CmdManager(object):
    '界面控制程序的类'
    def __init__(self,courseManager,database_dict):
        print "正在生产界面控制程序"
        self.main(courseManager,database_dict) ##界面针对指定的控制程序，与数据源做操作


    def print_help_info(self):
        """打印帮助信息"""
        print "XXXXX课程管理系统"
        print "输入1，打印出程序中存储的所有课程ID及课程名称"
        print "输入2，打印出课程数量"
        print "输入3，打印出最长的课程名称与其ID"
        print "输入4，删除最后一个课程并打印出剩余课程数量"
        print "输入5，根据提示新增一个课程"
        print "输入6，根据提示删除课程"
        print "输入7，退出程序"

    def any_key_c(self):
         print " "
         print " "
         if raw_input("输入回车键值继续........."):
            pass

    def case_wrong(self,str_in):
        #输入错误就提示
        print "您输入的" +str_in +"不是有效字符"
        self.any_key_c()


    def main(self,courseManager,database_dict):
     #主程序循环，通过if判断是否1-5，并执行对应的程序
     condition_1 = True
     while condition_1:
       self.print_help_info()
       str_choice = raw_input("请输入1-7选择一个指令")
       if str_choice.isdigit():
         int_choice = int(str_choice)
         if int_choice < 8 and int_choice > 0:
           if int_choice==1 :##打印出程序中存储的所有课程ID及课程名称
             courseManager.print_all_course(database_dict)
           if int_choice==2 :##打印出课程数量
             courseManager.get_coursenum(database_dict)
           if int_choice==3:##打印出最长的课程名称与其ID
             courseManager.print_longest(database_dict)
           if int_choice==4:##删除最后一个课程并打印出剩余课程数量
             courseManager.pop_newcourse(database_dict)
           if int_choice==5:##根据提示新增一个课程
             c_name=raw_input("请输入课程名字:")
             c_id=raw_input("请输入课程id:")
             c_create_date="2014-10-4"
             c_is_use='yes'
             courseManager.in_up_cour(database_dict,course(c_id,c_name,c_create_date,c_name))
           if int_choice==6:##根据提示删除课程
             d_id=raw_input("请输入要删除的课程id: ")
             courseManager.del_course(database_dict,d_id)
           if int_choice==7:##退出程序
                condition_1=False
                exit()
           continue
         else :
               self.case_wrong (str_choice)
               continue
       else :
             self.case_wrong (str_choice)
             continue