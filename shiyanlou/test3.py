
# -*- coding: utf8 -*-
__author__ = 'zr'
 # 1. 程序运行后可以循环输入操作命令
# 2. 操作命令输入0，打印出程序帮助信息，即每个操作命令的介绍
# 3. 操作命令输入1，打印出程序中存储的所有课程ID及课程名称
# 4. 输入2，打印出课程数量
# 5. 输入3，打印出最长的课程名称与其ID
# 6. 输入4，删除最后一个课程并打印出剩余课程数量
# 7. 输入5，退出程序
# 请独立完成程序，用到的知识点都在书中可以找到，遇到问题请及时提问，优秀的作业会展示在下周的实验文档中。
# 3.2 改进提示
# 可以使用下面的提示进行代码编写，也可以按照自己的理解来实现项目：
#按照mvc模型，model类由course类来组成，记录数据。
#           coursemanager类组成控制，控制逻辑接收前台命令，管理后台数据
            #cmdmanager类组成前台显示控制
            #但是我还是需要一个list做数据库保存已有的对象
# 8. 实现Course类和CourseManager类，分别实现课程及课程管理功能
# 9. 实现命令处理类CmdManager
class course(object):
    'couse 类，至少包含课程id，课程名称，使用属性返回和设置课程名称'
    __metaclass__=type
    def __init__(self,id,name,create_date,is_in_use):
        self.__id=id
        self.__name=name
        self.__create_date=create_date
        self.__is_in_use=is_in_use

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def create_date(self):
        return self.__create_date

    @create_date.setter
    def create_date(self,value):
        self.__create_date=value

    @property
    def is_in_use(self):
        return self.__is_in_use

    @is_in_use.setter
    def is_in_use(self,value):
        self.__is_in_use=value


# cs=course(1,'Python','2015-10-4','yes')
#
# print cs
# print cs.name
# print cs.create_date
# print cs.is_in_use
# print cs.id
    ##只有这个init函数会不会就了，不一定要set和get也可以？set和get只是更规范？
    ##是否需要用前下划线来标明这些属性不能外部直接使用？
# 10. Course类至少包括：
# • 课程ID（建议课程对象创建时自动生成）
# • 课程名称
# • 使用属性返回和设置课程名称Linux',2:'HTML',3:'HTML5',4:'NodeJS',5:'Shell',6:'Python'

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


# for k in data_con_dict.search_course_all():
#     print str(k.id)+k.name
#
# data_con_dict.del_course_id(5)
# data_con_dict.del_course(bootstrap)
#
# for k in data_con_dict.search_course_all():
#     print str(k.id)+k.name

#


# 11. CourseManager类成员至少包括：
# • 课程列表
# • 获取课程数量函数
# • 添加课程函数（参数为课程对象）
# • 删除最新课程函数
# • 删除课程函数（指定ID或指定课程名称）
# • 打印课程列表
# • 打印指定课程（指定ID或指定课程名称）


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

# 12. CmdManager类成员至少包括：
# • 支持的命令列表及每个命令的描述
# • 打印帮助信息
# • 命令处理函数
#  先是创建链接，然后获取资源，加载控制，加载界面
#
#
# 判断命令是否合法函数

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

# cm.get_coursenum(data_con_dict)
# cm.print_all_course(data_con_dict)
#
# cm.print_course_id(data_con_dict,5)
# cm.pop_newcourse(data_con_dict)
# cm.pop_newcourse(data_con_dict)
# cm.print_all_course(data_con_dict)
# cm.del_course(data_con_dict,4)
# cm.print_all_course(data_con_dict)
# cm.pop_newcourse(data_con_dict)
# cm.pop_newcourse(data_con_dict)
# cm.pop_newcourse(data_con_dict)
# cm.pop_newcourse(data_con_dict)
# cm.print_all_course(data_con_dict)
#