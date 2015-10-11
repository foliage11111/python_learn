# -*- coding: utf8 -*-

from clas_database import database_dict
import sys
sys.path.append('D:\\0tmpper\GitHub\python_learn\shiyanlou')
class courseManager(object):
    __metaclass__=type

    def print_longest(self,database_dict):
        '打印课程名字最长的那个'
        id_list=[]
        max_lex=0
        if database_dict.get_lenof_course():
            for k in database_dict.search_course_all():
                if len(k.name) >0:
                    if len(k.name)>max_lex:
                        max_lex=len(k.name)
                        del id_list[:]
                        id_list.append(k.name)
                    elif len(k.name)==max_lex:
                        id_list.append(k.name)
            if len(id_list) >0 :
                print "课程名字最长长度为"+str(max_lex)
                for i in id_list:
                    print "课程名字最长的是： "+ str(i)
        else:
            print "没有课程"


    def print_all_course(self,database_dict):
        "获取课程列表"
        for k in database_dict.search_course_all():
            print '课程ID为 '+str(k.id)+' ，课程名字为：'+k.name

    def print_course_id(self,database_dict,id):
        "根据id打印课程"
        c=database_dict.search_course(id)
        print  '课程ID为 '+str(c.id)+' ，课程名字为：'+c.name

    def get_coursenum(self,database_dict):
        "获取课程数量"
        print '课程总数量为: '+str(database_dict.get_lenof_course()) + ' 门课'

    def in_up_cour(self,database_dict,course):
        "插入或者更新课程"
        if database_dict.search_course(course.id):
            database_dict.in_up_course(course)
            print '已添加课程'+course.name
        else:
            database_dict.in_up_course(course)
            print '已更新id为'+str(course.id) +' 的课程'

    def pop_newcourse(self,database_dict):
        "查找id最大的一个课程，然后删除掉"
        id_list=[]
        if database_dict.get_lenof_course():
            for k in database_dict.search_course_all():
                id_list.append(k.id)
            database_dict.del_course_id(max(id_list))
            print '已删除最新添加课程：'
        else:
            print "数据库为空，无课程可以删除"



    def del_course(self,database_dict,id):
        "根据id或者名字删除课程"
        if id>=0:
            if database_dict.search_course(id):
                database_dict.del_course_id(id)
                print "已删除id为"+str(id)+" 的课程"
            else:
                print "不存在id为"+str(id) +" 的课程"
        else:
            print "输入有误，无法执行删除"

