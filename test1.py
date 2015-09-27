
#coding=GBK
# 1. 程序运行后可以循环输入操作命令
# 2. 操作命令输入0，打印出程序帮助信息，即每个操作命令的介绍
# 3. 操作命令输入1，打印出程序中存储的所有课程ID及课程名称
# 4. 输入2，打印出课程数量
# 5. 输入3，打印出最长的课程名称与其ID
# 6. 输入4，删除最后一个课程并打印出剩余课程数量
# 7. 输入5，退出程序
# 请独立完成程序，用到的知识点都在书中可以找到，遇到问题请及时提问，优秀的作业会展示在下周的实验文档中。
# 3.2 实现提示
# 可以使用下面的提示进行代码编写，也可以按照自己的理解来实现项目：
# 1. 使用while来实现接受输入的主循环
# 2. 使用input()获取命令输入
# 3. 使用printf()打印命令输出
# 4. 使用if-elif-else来处理不同的命令输入
# 5. 定义课程列表courses，每个元素包含课程ID和课程名称
# 6. 定义课程数组并使用下述课程名进行初始化，ID可随意：Linux,C++,HTML,HTML5,NodeJS,Shell,Python等。
# 7. 使用for或while访问课程列表并实现打印所有课程ID及名称，即操作命令1
# 8. 使用列表方法获取并打印courses长度，实现操作命令2
# 9. 使用for或while遍历课程列表，使用字符串方法查找最长的课程名称，实现命令3
# 10. 使用列表方法删除元素，实现操作命令4
# 11. 设置while循环的条件来实现break跳出循环，实现操作命令5
#
# 代码请放到文件夹/home/shiyanlou/Code/shiyanlou_cs421/lab1/中并提交到

# 1. 程序运行后可以循环输入操作命令
    # while 输入的内容不是0-5的时候，不停的要求输入，并提示需要输入0到5
dict_kecheng={1:'Linux',2:'HTML',3:'HTML5',4:'NodeJS',5:'Shell',6:'Python'}

def print_help_info ():
    print "XXXXX课程管理系统"
    print "输入1，打印出程序中存储的所有课程ID及课程名称"
    print "输入2，打印出课程数量"
    print "输入3，打印出最长的课程名称与其ID"
    print "输入4，删除最后一个课程并打印出剩余课程数量"
    print "输入5，退出程序"

def any_key_c():
 print " "
 print " "
 if raw_input("输入回车键值继续........."):
  pass

def case_1():
 #输入1，打印出程序中存储的所有课程ID及课程名称"
 for k in dict_kecheng :
   print "课程 "+str(k)+" 是： "+dict_kecheng.get(k)
 print "选课请返回主菜单"
 any_key_c()

def case_2():
 #输入2，打印出课程数量
  print "当前总共有" + str(len(dict_kecheng))+" 门课程。"
  print "选课请返回主菜单"
  any_key_c()

def case_3():
 #输入3，打印出最长的课程名称与其ID
 print "你选择3"
 dic4len={}
 list4dic_len=[]
 max_leeson=0
 if len(dict_kecheng.values()):
    for v in dict_kecheng.values() :
      list4dic_len.append(len(str(v)))
    max_leeson=max(list4dic_len)
    print "课程名称最长长度为"+str(max_leeson)
    dic4len=zip(list4dic_len,dict_kecheng.values())

    for k,j in dic4len :
      if k==max_leeson :
        print "课程名最长的是" + str(j)

    #print dic4len
 else :
  print "没有一个课程"
 #print dict_kecheng.get(max(dic4len.keys()))
 any_key_c()

def case_4():
 #输入4，删除最后一个课程并打印出剩余课程数量
 del_lesson=dict_kecheng.pop(len(dict_kecheng))
 print "已删除最后一个课程"+str(del_lesson)
 case_2()


def case_5():
 #输入5，退出程序
 print "退出程序，处理中。。。。"
 condition_1=False
 any_key_c()
 exit()

def case_wrong(str_in):
 #输入错误就提示
 print "您输入的" +str_in +"不是有效字符"
 any_key_c()


def main():
 #主程序循环，通过if判断是否1-5，并执行对应的程序
 condition_1 = True
 while condition_1:
   print_help_info()
   str_choice = raw_input("请输入1-5选择一个指令")
   if str_choice.isdigit():
     int_choice = int(str_choice)
     if int_choice < 6 and int_choice > 0:
       if int_choice==1 :
         case_1()
       if int_choice==2 :
         case_2()
       if int_choice==3:
         case_3()
       if int_choice==4:
         case_4()
       if int_choice==5:
         case_5()

       continue
     else :
           case_wrong (str_choice)
           continue
   else :
     case_wrong (str_choice)
     continue


main()
