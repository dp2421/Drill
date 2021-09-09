import turtle
for i in range (5):
    for j in range (5):
        for k in range (4):
            turtle.forward(100)
            turtle.left(90)
        turtle.forward(100)
    turtle.right(180)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

exitonclick()
