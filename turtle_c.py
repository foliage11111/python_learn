from swampy.TurtleWorld import *
from math import pi

r_len=input('input the length')  #shuru duobianxing de bianshu
world=TurtleWorld()
bob=Turtle()

def draw_n(len,t):##huayige duobianxing
 """"this function draw a turle.t means a object of turtle.and len is r
	len  si how long
	t is turttle
 """
 bob.delay = 0.001
 print t
 pd(t)
 angel_n=0.1 # angel erverytime
 turn_times=int(360/angel_n) #zhuan duoshaoci
 len_setp=2*pi*len/turn_times  #bu chang
 
 for i in range(turn_times):
  fd(t,len_setp)
  lt(t,angel_n)
 wait_for_user()

draw_n(r_len,bob)# kaishi zhixing 
