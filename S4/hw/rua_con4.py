from turtle import *
shape('blank')
color('blue')
speed(-1)

penup()
goto(-150,150)
pendown()

for i in range(6):
    for j in range(4):
        for k in range(4):
            forward(50)
            left(90)
        left(90)
    left(15)

penup()
goto(100, -100)
pendown()

for i in range(40):
    for j in range(4):
        forward(i*5)
        left(90)
    left(10)

penup()
goto(0,0)
pendown()

mainloop()
