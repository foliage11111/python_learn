#-*- coding:utf-8 -*-
import urllib
import socket
import cx_Oracle
import urllib
conn = cx_Oracle.connect('newdc/newdc@orcl')
cursor=conn.cursor()
url='http://img1.cache.netease.com/catchpic/6/6D/6DB67F617FA9F9002489E980C2E4250A.jpg'
idn = 'a'
filename = idn
data=urllib.urlopen(url).read()
sqlStr = "INSERT INTO image (id,filename,CONTENT) VALUES ('%s', '%s', :blobData)" % (idn, filename)
cursor.setinputsizes(blobData=cx_Oracle.BLOB)
cursor.execute(sqlStr, {'blobData':data})
cursor.execute('commit')
conn.close()
#----------------------先在数据库中创建表----------------------
#CREATE TABLE aurora(                                   
#id   VARCHAR2(10),                           
#filename    VARCHAR2(24),                             
#content    BLOB                                 
#);                           
