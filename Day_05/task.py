# Random password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
# Get number of letters from the user
nr_letters = int(input("How many letters would you like in your password?\n"))
# Get number of symbols from the user
nr_symbols = int(input(f"How many symbols would you like?\n"))
# Get number of numbers from the user
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - DONE!

# Randomize the lists
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

# Loop through the number of letters the user wants
i = 0
j = 0
k = 0
for letter in letters:
    if nr_letters > i:
        print(letters[i], end="")
        i += 1
for symbol in symbols:
    if nr_symbols > j:
        print(symbols[j], end="")
        j += 1
for number in numbers:
    if nr_numbers > k:
        print(numbers[k], end="")
        k += 1

# Hard Level - I tried.

# Randomize the lists
# random.shuffle(letters)
# random.shuffle(numbers)
# random.shuffle(symbols)

# Loop through the number of letters the user wants
# i = 0
# j = 0
# k = 0
# for letter in letters:
#     if nr_letters > i:
#         random_nums = random.shuffle(letters[i])
#         i += 1
# for symbol in symbols:
#     if nr_symbols > j:
#         print(symbols[j], end="")
#         j += 1
# for number in numbers:
#     if nr_numbers > k:
#         print(numbers[k], end="")
#         k += 1
# print(random_nums)
