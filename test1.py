s=4
f=8

j=[1,2,3,4,5,6,7,8]
for d in range(s):
 for  k in range(len(j)):   #用range和直接写j，会导致k的初始值不同，需要理解for的函数怎么写的
  print j[k]
