import turtle
from turtle import Turtle, Screen
import random

######################
# A simple turtle game
######################
# tim = Turtle(shape="turtle")            # Turtle 1
# tom = Turtle(shape="turtle")            # Turtle 2
# jill = Turtle(shape="turtle")           # Turtle 3
# chris = Turtle(shape="turtle")          # Turtle 4
# mitch = Turtle(shape="turtle")          # Turtle 5
# ben = Turtle(shape="turtle")            # Turtle 6

screen = Screen()                       # Screen object
screen.setup(width=500, height=400)     # Making the window size
is_race_on = False                      # Condition for the user to only start the game if
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles =[]
user_bet = screen.textinput(title="Make your bet!", prompt="Who will win the race? Enter a color: ")

# Loop that creates 6 turtles, sets a random color for each turtle and positions each
# turtle to the far left of the window
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while  is_race_on:

    for turtle in all_turtles:
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}!")
            else:
                print(f"You've lost. The winning color is {winning_color}.")
            is_race_on = False


# ben.penup()
# ben.goto(x=-220, y=115)
# ben.color(colors[0])
#
# mitch.penup()
# mitch.goto(x=-220, y=68)
# mitch.color(colors[1])
#
# chris.penup()
# chris.goto(x=-220, y=20)
# chris.color(colors[2])
#
# jill.penup()
# jill.goto(x=-220, y=-20)
# jill.color(colors[3])
#
# tom.penup()
# tom.goto(x=-220, y=-68)
# tom.color(colors[4])
#
# tim.penup()
# tim.goto(x=-220, y=-115)
# tim.color(colors[5])


screen.exitonclick()
