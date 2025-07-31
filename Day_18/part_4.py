from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color() -> tuple[int, int, int]:
    '''Returns a random color within a tuple'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

### Draws a random walk with tuples
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

def draw_spirogrpah(radius):
    '''Draws a spirograph based on the radius given'''
    for _ in range(int(360 / radius)):
        # New random color
        tim.color(random_color())
        # Draws a circle
        tim.circle(100)
        # Turns the tutle by the angle given
        turtle_head = tim.heading()
        tim.setheading(turtle_head + radius)

tim.speed("fastest")
draw_spirogrpah(5)


screen = Screen()
screen.exitonclick()
