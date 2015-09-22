from swampy.TurtleWorld import *

r_len=input('input the length')
r_n=input('input the number of angel:')
def draw_n(len,n):
 world=TurtleWorld()
 bob=Turtle()
 bob.delay = 0.01
 print bob
 pd(bob)
 angel_n=360.0/n

 for i in range(n):
  fd(bob,len)
  lt(bob,angel_n)

draw_n(r_len,r_n)
wait_for_user()
