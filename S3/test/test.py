colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import*
shape('turtle')
speed(-1)

for k in range(len(colors)):
    color(colors[k])
    begin_fill()
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)
mainloop()
