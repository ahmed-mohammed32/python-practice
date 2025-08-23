from turtle import Turtle
x_position = 0
y_position = 275
x_game_over_postion = 0
y_game_over_postion = 0
ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_position, y_position)
        self.score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)
        self.score += 1
    def game_over(self):
        self.goto(x_game_over_postion, y_game_over_postion)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)