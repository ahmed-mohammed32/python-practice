# Object Oriented Programming - Coffee Maker
# Report functionality is bugged

import sys

from Day_16.menu import MenuItem
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
# Coffee maker report object
report = CoffeeMaker()
# Coffee maker resources object
resources = CoffeeMaker()
# Drinks object
drink = Menu()
# Payment object
payment = MoneyMachine()

cost = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
        sys.exit()
    elif choice == 'report':
        resources.report()
        payment.report()
    elif choice in ['espresso', 'latte', 'cappuccino']:
        if resources.is_resource_sufficient(drink.find_drink(choice)):
            payment.make_payment(cost)
            report.make_coffee(drink.find_drink(choice))
