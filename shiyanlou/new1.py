# coding=utf8


import sqlite3

conn1=sqlite3.connect('D:\\0tmpper\GitHub\python_learn\shiyanlou\lesson3')

curs=conn1.cursor()
query1="select name from course where name='22'"
query1="delete  from course where id=(select max(id) from course) "
query1="insert into course(id,name,create_date,is_in_use) VALUES (?,?,?,?)"
query1="update course SET name=?,create_date=?,is_in_use=? where id=" +"'"+str(4)+"'"
list1=['op','3223','yes']
curs.execute(query1,list1)
conn1.commit()
# l1=curs.fetchall()
# if l1:
#     print ('212')
#     for i in l1:
#         print i[0]
# query1='create table course (id text,name text,create_date text ,is_in_use text)'
#
query2='select * from course'
#
# query3="insert into course VALUES ('5','Jnodes','2015-10-11','yes')"
# query4="insert into course VALUES ('3','HTML5','2015-10-11','yes')"
# query5="insert into course VALUES ('4','JavaScripts','2015-10-11','yes')"

# curs.execute(query3)
# curs.execute(query4)
# curs.execute(query5)
# conn1.commit()

curs.execute(query2)
for i in curs.fetchall():
    print i



conn1.close()