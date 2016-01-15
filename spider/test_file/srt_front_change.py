# -*- coding: utf8 -*-
#修改srt字母的字体格式和大小
__author__ = 'zr'


import re


# txt_buff = open("c:\\Users\\zr\\Desktop\\trace_songjiao.txt",'r')
url1='d:\\0tmpper\\GitHub\\python_learn\\spider\\test_file\\The Revenant (2015) .srt'
txt_buff = open(url1,'r')
# contest=txt_buff.read()
re1=re.compile(r'-->',re.S)  ##用来匹配字幕里面的时间，实际情况还要看字幕里面的内容
re2=re.compile(r'[A-Za-z]+') ##用来匹配英文字幕
switch1=False
newcontext=''
# print txt_buff.read()
for k in txt_buff.readlines():
#由于不能识别中文，所以每次只能识别中文上面一行的特殊字符，然后下次进来的时候给加上
#英文则可以每次匹配了之后就加上
#只要文件不超过内存大小就一直这么做
#默认 换行符号在最后，所以没影响
    if switch1 :
        # print '{\\fs25}'+k
        newcontext=newcontext+'{\\fs21}'+k
        switch1=False
    elif re2.search(k):
        # print '{\\fs25}'+k
        newcontext=newcontext+'{\\fs18}'+k
    else :
        newcontext=newcontext+k
        # print k
    if re1.search(k):
        switch1=True
# '{\fs25}'
txt_buff.close()
txt_buff2 = open(url1+'.backup','w')
txt_buff2.write(newcontext)
txt_buff2.close()
