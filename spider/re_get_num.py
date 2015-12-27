# -*- coding: utf8 -*-
#取得当前的中奖号码
__author__ = 'zr'

import re
import os

txt_buff = open("c:\\Users\\zr\\Desktop\\ssq_test1.txt",'r')
contents=''
switch1=False
for i  in txt_buff.readlines():
    if i.strip()=='<tbody>':
        switch1=True
    if i.strip() == '</tbody>':
        switch1=False
    if switch1 :
       contents=contents+i.strip()
print contents
txt_buff.close()
ssq_list=re.findall(r'<td>\d{7}.*?"blue">\d{2}</td>', contents)
print ssq_list[0]

