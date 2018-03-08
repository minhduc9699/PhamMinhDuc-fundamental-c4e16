
from turtle import *

shape('arrow')
color('red')
penup()
goto(-100,100)
pendown()

from turtle import*
speed(-100)
color('red')

right(30)
for i in range(4):
    forward(50)
    left(240/4)
    forward(50)
    left(180-240/4)
    forward(50)
    left(240/4)
    forward(50)
    right(180-120/4)

penup()
goto(100,-100)
pendown()

left(30)
so_canh = 6
lenght = 100
for l in range(so_canh):
    if so_canh == 5 or so_canh == 3:
        color('blue')
    else:
        color('red')
    for l in range(so_canh):
        forward(lenght)
        left(360/so_canh)
    so_canh -= 1













mainloop()

'''
from turtle import *
color("red")
def draw(deg):
    left(deg)
    left(30)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    home()

for  i in range(0,360,90):
    draw(i)

mainloop()
'''
