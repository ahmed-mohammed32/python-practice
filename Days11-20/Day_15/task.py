##### For tranparencey, I'm not afraid to show my failures.                      #####
##### I had to look at the solution and modifiy it to work for my original code  #####

# Coffee Machine Project


from data import menu, resources
import sys

# Prompt user for what they would                                       #####DONE#####
    ## If they type 'report', display the current resources. i.e. the   #####DONE#####
    #  resources dictionary
# Prompt user for coins                                                 #####DONE#####
# Ask how many quarters                                                 #####DONE#####
# Ask how many dimes                                                    #####DONE#####
# Ask how many nickles                                                  #####DONE#####
# Ask how many pennies                                                  #####DONE#####
# Prompt the user's change
# Prompt the drink that they got
# Loop everything


def get_report(drink_resources, change):
    """Prints report"""
    water = drink_resources["water"]
    milk = drink_resources["milk"]
    coffee = drink_resources["coffee"]
    return f"Water: {water}ml\n" f"Milk: {milk}ml\n" f"Coffee: {coffee}g\n" f"Money:${change}"

def check_resources(drink_ingredients):
    # """Checks if drinks have enough resources"""
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


    # Espresso
    # drink_1_water  = drink_resources["espresso"]["ingredients"]["water"]
    # drink_1_coffee = drink_resources["espresso"]["ingredients"]["coffee"]
    # # Latte
    # drink_2_water  = drink_resources["latte"]["ingredients"]["water"]
    # drink_2_milk   = drink_resources["latte"]["ingredients"]["milk"]
    # drink_2_coffee = drink_resources["latte"]["ingredients"]["coffee"]
    # # Cappuccino
    # drink_3_water  = drink_resources["cappuccino"]["ingredients"]["water"]
    # drink_3_milk   = drink_resources["cappuccino"]["ingredients"]["milk"]
    # drink_3_coffee = drink_resources["cappuccino"]["ingredients"]["coffee"]
    # if (drink_1_water or drink_2_water or drink_3_water) == 0:
    #     return "Sorry there is not enough water."
    # if (drink_1_coffee or drink_2_coffee or drink_3_coffee) == 0:
    #     return "Sorry there is not enough coffee."
    # if (drink_2_milk or drink_3_milk) == 0:
    #     return "Sorry there is not enough milk."


def process_coins():
    # """Checks if there are enough resources, then asks user for coins and calculates the total values of coins"""
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted,
    or False when money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print (f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}")


profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Print the report
    if choice == 'report':
        print(get_report(resources, profit))
    elif choice == 'off':
        sys.exit()
    elif choice in ['espresso', 'latte', 'cappuccino']:
        drink = menu[choice]

        # 1st, check if we have enough resources
        if check_resources(drink["ingredients"]):
            # 2nd, process the coins
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
