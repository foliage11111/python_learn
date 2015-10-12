# -*- coding: utf8 -*-

from class_course import course
import sys
import sqlite3
sys.path.append('D:\\0tmpper\GitHub\python_learn\shiyanlou')
class courseManager(object):
    __metaclass__=type

    def getConnect(self):
        self.__conn1=sqlite3.connect('D:\\0tmpper\GitHub\python_learn\shiyanlou\lesson3')


    def print_all_course(self):
        "获取课程列表"
        self.getConnect()
        curs=self.__conn1.cursor()
        query2='select id,name from course'
        curs.execute(query2)
        list1=curs.fetchall()
        if list1:
             return list1
             self.__conn1.close()
        else:
            self.__conn1.close()
            return ['空课程表']


    def print_course_id(self,id):
        "根据id打印课程"
        self.getConnect()
        curs=self.__conn1.cursor()
        query2="select id,name from course where id="+"\'"+str(id)+"\'"
        curs.execute(query2)
        list1=curs.fetchall()
        if list1:
             return list1
             self.__conn1.close()

        else:

            self.__conn1.close()
            return [('','')]

    def in_cour(self,list1):
        "插入或者更新课程"
        self.getConnect()
        curs=self.__conn1.cursor()
        query1="insert into course(id,name,create_date,is_in_use) VALUES (?,?,?,?)"
        curs.execute(query1,list1)
        self.__conn1.commit()
        self.__conn1.close()
        print '已更新id为'+str(course.id) +' 的课程'
        return True

    def up_cour(self,course):
        "插入或者更新课程"
        if self.print_course_id(course.id):
            self.getConnect()
            curs=self.__conn1.cursor()
            list1=[course.id,course.name,course.create_date,course.is_in_use]
            query1="update course SET name=?,create_date=?,is_in_use=? where id=" +"'"+str(course.id)+"'"
            curs.execute(query1,list1)
            self.__conn1.commit()
            self.__conn1.close()
            print '已更新id为'+str(course.id) +' 的课程'
        else:
            print "不存在该值"
            return False



    def del_course(self,id):
        "根据id或者名字删除课程"
        if self.print_course_id(id):
            self.getConnect()
            curs=self.__conn1.cursor()
            query1="delete  from course where id="+"'"+str(id)+"'"
            curs.execute(query1)
            list1=curs.fetchall()
            self.__conn1.commit()
            self.__conn1.close()
            return True
        else:
            return False