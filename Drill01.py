import turtle

def move_left():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def move_right():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def move_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def move_down():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

turtle.shape('turtle')

turtle.onkey(move_left,'d')
turtle.onkey(move_right,'a')
turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.listen()
    
turtle.exitonclick()
