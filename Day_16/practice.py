from turtle import Turtle, Screen
from another_module import another_variable
from prettytable import PrettyTable
print(another_variable)

# # Create a new object from a Blueprint
# timmy = Turtle()
# print(timmy)
#
# # Call methods that are associated with that object
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
#
# # Create a new object from a Blueprint
# my_screen = Screen()
#
# # Tap into it's attribute
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Create the table object
table = PrettyTable()
# Add 2 columns to the object with the add_column method
table.add_column("Pokemon",
                 ["Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Type",
                  ["Fire", "Water", "Grass"])

# Set all columns to the left with the 'align' attribute
table.align = "l"

print(table)
