#############
# Snake game
#############

from turtle import Screen, Turtle

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x_position = [0, -20, -40]
all_squares = []                              # All of the squares

# Loop that creates 3 squares next to each other on the left
for square_index in range(0, 3):
    new_square = Turtle(shape="square")       # Turtle object
    new_square.color("white")
    new_square.penup()
    new_square.goto(x=x_position[square_index], y=0)
    all_squares.append(new_square)


game_is_on = True
while game_is_on:
    for squares in all_squares:
        squares.forward(20)


screen.exitonclick()
