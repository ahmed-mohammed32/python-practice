# Paddles for player 1 & 2
from turtle import Turtle
starting_positions = [40, 20, 0, -20, -40]

class Paddle():
    def __init__(self, coordinates):
        self.all_paddles = []
        self.x_position = coordinates[0]
        self.y_position = coordinates[1]
        self.create_paddle()
    def create_paddle(self):
        for position in starting_positions:
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.penup()
            paddle.goto(self.x_position, self.y_position + position)
            self.all_paddles.append(paddle)
    def up(self):
        # Move each paddle segment up by 20 pixels
        for segment in self.all_paddles:
            new_y = segment.ycor() + 20
            segment.goto(segment.xcor(), new_y)
    def down(self):
        # Move each paddle segment down by 20 pixels
        for segment in self.all_paddles:
            new_y = segment.ycor() - 20
            segment.goto(segment.xcor(), new_y)
