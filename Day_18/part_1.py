from turtle import Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# Make a square
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

# Make a square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# Dashed lines
for _ in range(20):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
