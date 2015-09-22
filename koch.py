#!/usr/bin/env python

from swampy.TurtleWorld import *

def draw_koch_detail(t,length,n):
    if  n-1>0:
      draw_koch_detail(t,length,n-1)
    else:
      fd(t,length)
    lt(t,60)
    if  n-1>0:
      draw_koch_detail(t,length,n-1)
    else:
      fd(t,length)
    rt(t,120)
    if  n-1>0:
      draw_koch_detail(t,length,n-1)
    else:
      fd(t,length)
    lt(t,60)
    if  n-1>0:
      draw_koch_detail(t,length,n-1)
    else:
      fd(t,length)
      
  
 
 
def draw_koch_detail2(t,length,n):
    if  n-1==0:
        fd(t,length)
        return
    
    draw_koch_detail2(t,length,n-1)
   
    lt(t,60)
    
    draw_koch_detail2(t,length,n-1)
    
    rt(t,120)
    
    draw_koch_detail2(t,length,n-1)
    
    lt(t,60)
    
    draw_koch_detail2(t,length,n-1)
    
      
             
world=TurtleWorld()
bob=Turtle()
bob.delay = 0.001
draw_koch_detail2(bob,4,4)

wait_for_user()
