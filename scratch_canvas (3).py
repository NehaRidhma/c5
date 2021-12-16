import turtle

turtle.shape('turtle')
turtle.pencolor('red')
for x in range(0, 19):
    turtle.forward(100)
    if(x % 2 == 0):
        turtle.left(175)
    else:
        turtle.left(225)