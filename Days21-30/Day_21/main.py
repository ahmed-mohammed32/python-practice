###########
# Pong game
###########
from turtle import Turtle, Screen
from paddle import Paddle

# Step 1 - Set up the screen
# Step 2 - Create the paddles

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Create the paddles
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
