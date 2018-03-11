from turtle import *
shape('turtle')
color('blue')
speed(-1)

penup()
goto(-100,100)
pendown()

for i in range(1, 30):
    for j in range(4):
        forward(50)
        left(90)
    left(15)

penup()
goto(100, -100)
pendown()

for i in range(1,30):
    for j in range(4):
        forward(i+10)
        left(90)
    left(15)

penup()
goto(0,0)
pendown()

mainloop()
