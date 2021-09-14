import turtle
import random

def drunken_movew():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def drunken_movea():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_moves():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def drunken_moved():
    turtle.setheading(360)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(drunken_movew, 'w')
turtle.onkey(drunken_movea, 'a')
turtle.onkey(drunken_moves, 's')
turtle.onkey(drunken_moved, 'd')

turtle.onkey(restart, 'Escape')
turtle.listen()
