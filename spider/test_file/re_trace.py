# -*- coding: utf8 -*-
#格式化trace 文件中cpu和elapse 字段最长的
__author__ = 'zr'


import re


# txt_buff = open("c:\\Users\\zr\\Desktop\\trace_songjiao.txt",'r')
txt_buff = open("d:\\0tmpper\\GitHub\\python_learn\\spider\\test_file\\trace_songjiao2.txt",'r')
contest=txt_buff.read()
p0=re.compile(r'total(.*?)Misses in library cache during parse',re.S)
#本例再次复习了一下要取什么东西，关键在于这个re.s，可以跳过换行符号
# #当然我在双色球里面的处理办法也没错，因为自动换行了省去了我一些功夫，得到list也不会跟元组混在一起结果就没的解放出来
trace_list=p0.findall(contest)
txt_buff.close()
p1 = re.compile('(\d)\s+?(\d+\.\d+?)\s+?(\d+\.\d+?)\s',re.S)
##本例复习了一下到底要取什么东西\s表示空格符号；（）才是你想要的内容，可惜括号都变成了元组
total_list=[]
for i in trace_list:
    total_list.append(p1.findall(i)[0])
# print trace_list[11].strip()
# print p1.findall(trace_list[11])
# 5      0.00       0.01          0          0          0           2
# [('5', '0.00', '0.01')]
cpu_list=[]
elapsed_list=[]
for k in total_list:
    print k
    cpu_list.append(k[1])
    elapsed_list.append(k[2])
cpu_list.pop()
elapsed_list.pop()
print 'cpu: '+max(cpu_list)+'  elapsed:  '+max(elapsed_list)


