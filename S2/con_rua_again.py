from turtle import *

shape('arrow')
color('red')
speed(-1)

penup()
goto(-100,100)
pendown()

for i in range(4):
    for j in range(2):
        forward(50)
        left(45)
        forward(50)
        left(135)
    left(90)

penup()
goto(100,-100)
pendown()

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
