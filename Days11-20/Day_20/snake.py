from turtle import Turtle
starting_positions = [0, -20, -40]
up = 90
down = 270
right = 0
left = 180

class Snake:
    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]
    def create_snake(self):
        # Loop that creates 3 squares next to each other left on the x-axis
        for position in starting_positions:
            self.add_segment((position, 0))
    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.all_squares.append(new_square)
    def extend(self):
        self.add_segment(self.all_squares[-1].position())
    def move(self):
        for squ_num in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[squ_num - 1].xcor()
            new_y = self.all_squares[squ_num - 1].ycor()
            self.all_squares[squ_num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        '''Move the snake up and doesn't let it go backwards'''
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        '''Move the snake down and doesn't let it go up'''
        if self.head.heading() != up:
            self.head.setheading(down)
    def right(self):
        '''Move the snake right and doesn't let it go left'''
        if self.head.heading() != left:
            self.head.setheading(right)
    def left(self):
        '''Move the snake left and doesn't let it go right'''
        if self.head.heading() != right:
            self.head.setheading(left)

