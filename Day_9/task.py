# Blind Auction project

import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# Print 100 new lines so that the next person can't see the previous bid
# print("Hello")
# print("\n" * 100)

# Data dictionary
data = {}

# Ask fuction
def ask_name_and_price():
    name = input("What is your name?: ")
    price = input("What is your bid?: $")
    return name, price

# Loop till user says no
done = False

while not done:
        # Player's names and bid price amount
        name, price = ask_name_and_price()
        data[name] = price
        ask_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
        if ask_bidder == 'yes':
            print("\n" * 15)
        elif ask_bidder == 'no':
            done = True

max_bidder = max(data, key=data.get)
max_value = data[max_bidder]

print(f"The winner is {max_bidder} with a bid of ${max_value}")

