# coding=utf8 -*-
__author__ = 'zr'
import os

#os.mknod("c:\\Users\\zr\\Desktop\\ssq_test1.txt")  #在桌面新增一个txt文件

char = '<td>2015152</td><td>2015-12-27 21:30(xe6x97xa5)</td><td class="red">11&nbsp;18&nbsp;19&nbsp;21&nbsp;29&nbsp;32</td><td class="blue">12</td>'

print char[4:11]+','+char[char.find('\"red\">')+6:char.find('</td><td class=\"blue\">')].replace('&nbsp;',',')+','+char[char.find('\"blue\">')+7:len(char)-5]

