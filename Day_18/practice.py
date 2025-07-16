from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


color_names = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque',
    'blanchedalmond', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
    'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'darkblue',
    'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta',
    'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon',
    'darkseagreen', 'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet',
    'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick', 'floralwhite',
    'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod',
    'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki',
    'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue',
    'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgreen', 'lightgrey',
    'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray',
    'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'maroon',
    'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
    'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
    'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin',
    'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered',
    'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred',
    'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple',
    'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen',
    'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow',
    'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise',
    'violet', 'wheat', 'whitesmoke', 'yellowgreen', 'white', 'black', 'red', 'green',
    'blue', 'cyan', 'yellow', 'magenta', 'grey']


# Make a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# Make a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Dashed lines
# for _ in range(20):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()

# Set the turtle object to a random color
def random_color():
    return timmy_the_turtle.color(random.choice(color_names))

# Draw a triangle
def draw_triangle(tri_sides):
    angle = 360 / tri_sides
    for _ in range(3):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(120)

# Draw a square
def draw_square(squ_sides):
    angle = 360 / squ_sides
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# Draw a pentagon
def draw_pentagon(pen_sides):
    angle = 360 / pen_sides
    for _ in range(5):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# Draw a hexagon
def draw_hexagon(hex_sides):
    angle = 360 / hex_sides
    for _ in range(6):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# Draw a heptagon
def draw_heptagon(hep_sides):
    angle = 360 / hep_sides
    for _ in range(7):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# Draw a octagon
def draw_octagon(oct_sides):
    angle = 360 / oct_sides
    for _ in range(8):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# Draw a nonagon
def draw_nonagon(non_sides):
    angle = 360 / non_sides
    for _ in range(9):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# Draw a decagon
def draw_decagon(dec_sides):
    angle = 360 / dec_sides
    for _ in range(10):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


shapes = [
    (draw_triangle, 3),
    (draw_square, 4),
    (draw_pentagon, 5),
    (draw_hexagon, 6),
    (draw_octagon, 8),
    (draw_nonagon, 9),
    (draw_decagon, 10),
]

for draw_shape, sides in shapes:
    timmy_the_turtle.color(random.choice(color_names))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()
