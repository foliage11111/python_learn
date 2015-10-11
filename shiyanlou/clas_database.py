
# -*- coding: utf8 -*-
__author__ = 'zr'

from class_course import course
import sys
sys.path.append('D:\\0tmpper\GitHub\python_learn\shiyanlou')

class database_dict(object):
    "这是一个数据库类型，模拟数据库层，用一个字典记录所有数据，以id作为key，对象作为value"
    def __init__(self):
        self.__Data_Course={}

    def in_up_course(self,course):  ##更新或者插入数据课程
        self.__Data_Course[course.id]=course

        return 'done'

    def del_course(self,course):
        if self.__Data_Course[course.id]:
            del self.__Data_Course[course.id]
            print "删除成功"
        else:
            print "删除失败"
            return " 没有这个课程"

    def del_course_id(self,id):
        if self.__Data_Course[id]:
            del self.__Data_Course[id]
        else:
            print "删除失败"
            return " 没有这个id的课程"

    def search_course(self,id):  ##id搜索课程
        if self.__Data_Course.has_key(id) :
             return self.__Data_Course[id]
        else:
            return False

    def search_course_all(self):  ##获取所有课程
        return self.__Data_Course.itervalues()

    def get_lenof_course(self):  ##获取课程总数
        return  len(self.__Data_Course.keys())
        return  len(self.__Data_Course.keys())