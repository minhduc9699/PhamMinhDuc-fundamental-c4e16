from turtle import *

mau = ['red', 'blue', 'brown', 'yellow', 'grey']

penup()
goto(-100,100)
pendown()

so_canh = 3
i = 0
for j in range(so_canh,8):
    while i < len(mau):
        color(mau[i])
        i += 1
        for k in range(so_canh):
            forward(50)
            left(360/so_canh)
        so_canh += 1

penup()
goto(50,100)
pendown()
l = 0
for i in range(5):
    while l < len(mau):
        color(mau[l])
        fillcolor(mau[l])
        l += 1
        begin_fill()
        for i in range(2):
            forward(50)
            left(90)
            forward(100)
            left(90)
        end_fill()
        forward(50)




mainloop()
