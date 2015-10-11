
# -*- coding: utf8 -*-
__author__ = 'zr'

class course(object):
    'couse 类，至少包含课程id，课程名称，使用属性返回和设置课程名称'
    __metaclass__=type
    def __init__(self,id,name,create_date,is_in_use):
		'初始化必须输入id，name，创建日期,以及是否在用'
        self.__id=id
        self.__name=name
        self.__create_date=create_date
        self.__is_in_use=is_in_use

    @property
    def id(self):
		'id属性的取值函数'
        return self.__id

    @id.setter
    def id(self,value):
		'id属性的设置函数'
        self.__id=value

    @property
    def name(self):
		'name属性的取值函数'
        return self.__name

    @name.setter
    def name(self,value):
		'name属性的设置函数'
        self.__name=value

    @property
    def create_date(self):
		'创建日期的取值函数'
        return self.__create_date

    @create_date.setter
    def create_date(self,value):
		'创建日期的设置函数'
        self.__create_date=value

    @property
    def is_in_use(self):
		'是否在用的取值函数'
        return self.__is_in_use

    @is_in_use.setter
    def is_in_use(self,value):
		'是否在用的设置函数'
        self.__is_in_use=value

 