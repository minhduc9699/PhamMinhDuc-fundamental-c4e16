from turtle import *
shape('turtle')
color('green')
fillcolor('yellow')

begin_fill()
#circle
for i in range(5):
    circle(20)
    left(360/30)
penup()
goto(-90, -90)
pendown()

for i in range(4):
    forward(100)
    left(90)
end_fill()


mainloop()
