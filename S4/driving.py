from turtle import *

def h1():
    forward(100)
def h2():
    left(45)
def h3():
    right(45)
def h4():
    backward(100)
def h5():
    bye()

onkey(h1, 'Up')
onkey(h2, 'Left')
onkey(h3, 'Right')
onkey(h4, 'Down')
onkey(h5, 'q')

listen()
mainloop()
