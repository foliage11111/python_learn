# -*- coding: utf8 -*-

from class_course import course
import sys
import sqlite3
sys.path.append('D:\\0tmpper\GitHub\python_learn\shiyanlou')
class courseManager(object):
    __metaclass__=type

    def getConnect(self):
        self.__conn1=sqlite3.connect('D:\\0tmpper\GitHub\python_learn\shiyanlou\lesson3')

    def print_longest(self):
        '打印课程名字最长的那个'
        self.getConnect()
        curs=self.__conn1.cursor()
        query1="select max(name) from course"     #改成按字符串长度来查找的
        curs.execute(query1)
        list1=curs.fetchall()
        if list1:
             print "课程名字最长长度为"+str(len(str(list1[0][0])))
             for i in list1:
                 print "课程名字最长的是： "+ str(i[0])
             self.__conn1.close()
        else:
            print "没有课程"
            self.__conn1.close()


    def print_all_course(self):
        "获取课程列表"
        self.getConnect()
        curs=self.__conn1.cursor()
        query2='select id,name from course'
        curs.execute(query2)
        list1=curs.fetchall()
        if list1:
             for k in list1:
               print '课程ID为 '+str(k[0])+' ，课程名字为：'+ str(k[1])
             self.__conn1.close()
        else:
            self.__conn1.close()
            print '空课程表'


    def print_course_id(self,id):
        "根据id打印课程"
        self.getConnect()
        curs=self.__conn1.cursor()
        query2="select id,name from course where id="+"\'"+str(id)+"\'"
        curs.execute(query2)
        list1=curs.fetchall()
        if list1:
             for k in list1:
                  print '课程ID为 '+str(k[0])+' ，课程名字为：'+str(k[1])
             self.__conn1.close()
             return True
        else:
            print '没有这门课'
            self.__conn1.close()
            return False

    def get_coursenum(self):
        "获取课程数量"
        self.getConnect()
        curs=self.__conn1.cursor()
        query1="select count(*) from course"
        curs.execute(query1)
        list1=curs.fetchall()
        if list1:
             for k in list1:
                   print '课程总数量为: ' +str(k[0]) + ' 门课'

        else:
            print '空课程表'
        self.__conn1.close()


    def in_cour(self,course):
        "插入或者更新课程"
        if self.print_course_id(course.id):
            return "已经有了这个值"
        self.getConnect()
        curs=self.__conn1.cursor()
        list1=[course.id,course.name,course.create_date,course.is_in_use]
        query1="insert into course(id,name,create_date,is_in_use) VALUES (?,?,?,?)"
        curs.execute(query1,list1)
        self.__conn1.commit()
        self.__conn1.close()
        print '已更新id为'+str(course.id) +' 的课程'

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

    def pop_newcourse(self):
        "查找id最大的一个课程，然后删除掉"
        self.getConnect()
        curs=self.__conn1.cursor()
        query1="delete  from course where id=(select max(id) from course) "
        curs.execute(query1)
        self.__conn1.commit()
        self.__conn1.close()
        print '已删除最新添加课程：'


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
            print "已删除id为"+str(id)+" 的课程"