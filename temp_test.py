#!/usr/bin/env python
#coding=utf8
#import re
#emphasis_pattern=r'\*([^\*]+)\*'
#print re.sub(emphasis_pattern,r'<em>\1</em>','hello,*python*')


dict_kecheng={1:'Linux',2:'HTML',3:'HTML5',4:'NodeJS',5:'Shell',6:'Python'}



l1=dict_kecheng.values()
l1.reverse()
print l1

l2=sorted(dict_kecheng.items(),lambda x,x1:x1,reverse=True)

# for x in range(0,100):
#     print ('age %s' %(x*2))
#     if (x+1)*2>25:
#         break

print 'l2'
print l2
print len(dict_kecheng)

print dict_kecheng.items()

print dict_kecheng.iteritems()

print dict_kecheng.viewitems()

print dict_kecheng[dict_kecheng.keys()[-1]]

# for k,j in dict_kecheng.iteritems() :
#     print k
#     print j

red1=5
red2=13
red3=9
red4=22
red5=30
red6=19
blue1=4

statement1='print '+'red1+red2+red3+red4+red5'

exec(statement1)