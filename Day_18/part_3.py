from turtle import Turtle, Screen
import random

arrow = Turtle()
arrow.shape("arrow")

# Random colors
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

arrow.color(random.choice(color_names))

def random_color():
    return arrow.color(random.choice(color_names))

def move_arrow():
    '''Moves the arrow in a random direction with a new color each time it changes direction'''
    east = 0
    north = 90
    west = 180
    south = 270
    directions = [0, 90, 180, 270]
    moving = True
    # Loop that keeps the arrow going forward
    while moving:
        for _ in directions:
            arrow.setheading(random.choice(directions))
            arrow.pensize(random.randint(5, 7))
            arrow.forward(random.randint(1, 50))
            random_color()
            # arrow.setheading(south)
            # random_color()
            # arrow.pensize(random.randint(5, 7))
            # arrow.forward(random.randint(1, 50))
            # arrow.setheading(east)
            # random_color()
            # arrow.pensize(random.randint(5, 7))
            # arrow.forward(random.randint(1, 50))
            # arrow.setheading(west)
            # random_color()
            # arrow.pensize(random.randint(5, 7))
            # arrow.forward(random.randint(1, 50))


move_arrow()

# Create a screen for our object
screen = Screen()
screen.bgcolor("black")
screen.exitonclick()
