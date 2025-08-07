from turtle import Turtle, Screen

#####################
# Etch-A-Sketch App #
#####################

def move_forwards():
    '''Moves the turtle forwards'''
    turtle.forward(10)

def move_backward():
    '''Moves the turtle backwards'''
    turtle.backward(10)

def move_left():
    '''Moves the turtle direction to the left'''
    turtle.left(10)

def move_right():
    '''Moves the turtle direction to the right'''
    turtle.right(10)

def clear_screen():
    '''Clears the screen and moves the turtle to the starting point'''
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle = Turtle()                                   # Turtle object
screen = Screen()                                   # Screen object

screen.listen()                                     # Listen to user inputs
screen.onkey(fun=move_forwards, key="w")            # Practice with keyboard clicks & higher order functions
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()
