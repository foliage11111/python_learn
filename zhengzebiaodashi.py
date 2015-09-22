#!/usr/bin/env python
import re

rule1=re.compile(r'^[0-9a-zA-Z][0-9a-zA-Z._]{1,10}@[a-zA-Z]{1-18}[.][c][o][m]$')

rule2=re.compile(r'^[0-9a-zA-Z][0-9a-zA-Z._]{1,10}@[a-zA-Z]{1,18}[.][c][o][m]$')## email pipei


rule3=re.compile(r'^\w[0-9a-zA-Z._]{1,19}[0-9a-zA-Z]@[a-zA-Z]{1,18}[.][c][o][m]$')## email pipei

rule4=r'(\w+|(\w+.\w+?))\@(\w+?)\.(com|net|org|gov|cn|com.cn)$' #jiewei zheyang jiu zhengque le
#\d pipei shuzi  \D not shuzi

email1='someone@gmail.com'
email2='bill.gates@microsoft.com';
email3='lin.chole@deacthlon.com';
res1=re.match(rule4,email1)
if res1:
    print res1.group(0)
else:
    print res1
    
res1=re.findall(rule4,email1)
if res1:
    print res1
else:
    print res1

res2=re.match(rule4,email3)
if res2:
    print res2.group(0)
else:
    print res2