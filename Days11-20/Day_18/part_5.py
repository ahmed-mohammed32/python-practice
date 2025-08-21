import turtle
import random
from turtle import Screen

# import colorgram

# # Extract the image
# colors = colorgram.extract('image.jpg', 30)
#
# color = 0
# color_list = []
# for _ in colors:
#     # Get the 1st color index
#     first_color = colors[color]
#     # Get 1st color index as just the namedtuple value
#     rgb_namedtuple = first_color.rgb
#     # Convert the namedtuple to a normal tuple
#     rgb_tuple = tuple(rgb_namedtuple)
#
#     color_list.append(rgb_tuple)
#     color += 1
#
# print(color_list)

##############################
## DRAWING A HIRST PAINTING ##
##############################

def random_color(rgb_list) -> tuple[int, int, int]:
    '''Returns a random color within a tuple'''
    random_rgb_color = random.choice(rgb_list)
    return random_rgb_color

def plot_dots() -> None:
    '''Plot the dot of the Hirst Painting'''
    for _ in range(10):
        color = random_color(image_color_list)     # Get a random color
        pen.dot(20, color)             # Draw a dot on the screen
        pen.penup()                                # Pick up the pen
        pen.forward(50)                            # Go forward by 50 spaces


# List of tuple RGB values from painting
image_color_list = [(232, 241, 239), (1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]

x = -200                                        # X coordinates to start
y = -200                                        # Y coordinates to start
turtle.colormode(255)                           # Sets turtle mode to use RGB color values (0-225)
pen = turtle.Turtle()                           # Turtle object
pen.penup()                                     # Pick the pen up
pen.goto(x, y)                                  # Set the pen to the bottom left position on the screen
pen.speed("fastest")                            # Set the pen speed to the fastest

for _ in range(10):                            # Loop to plot X and Y 10 times and go up by 50 spaces on the Y axis
    plot_dots()
    y += 50
    pen.goto(x, y)

pen.hideturtle()
screen = Screen()
screen.exitonclick()