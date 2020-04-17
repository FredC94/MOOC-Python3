import turtle
for i in range(3):
    angle = 120
    for j in range(4):
        angle = 180 - angle
        turtle.left(angle)
        turtle.forward(100)
    turtle.right(120)

turtle.hideturtle()
turtle.done()