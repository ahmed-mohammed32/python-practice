# Calculator project

import art
print(art.logo)

# Allows you to store the add method into a variable and use that variable as the add method
#
# my_favorite_op = add
# print(my_favorite_op(2, 3))

# Add method
def add(n1, n2):
    return n1 + n2

# Subtract method
def subtract(n1, n2):
    return n1 - n2

# Multiply method
def multiply(n1, n2):
    return n1 * n2

# Divide method
def divide(n1, n2):
    return n1 / n2

# Calculation checking method
def calculations_check(first_num,second_num):
    if op_choice == '+':
        answer = operators["+"](first_num, second_num)
        print(f"{first_num} {op_choice} {second_num} = {answer}" )
        return answer
    elif op_choice == '-':
        answer = operators["-"](first_num, second_num)
        print(f"{first_num} {op_choice} {second_num} = {answer}")
        return answer
    elif op_choice == '*':
        answer = operators["*"](first_num, second_num)
        print(f"{first_num} {op_choice} {second_num} = {answer}")
        return answer
    elif op_choice == '/':
        answer = operators["/"](first_num, second_num)
        print(f"{first_num} {op_choice} {second_num} = {answer}")
        return answer



# Operators and methods are stored as key value pairs in a dictionary
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Method call with the dictionary
# print(operators["*"](4, 8))
done = False
while not done:
    should_continue = True
    first_num       = float(input("What's the first number?: "))

    while should_continue:
        # Ask user for numbers and operation
        for operator in operators:
            print(operator)
        op_choice  = input("Pick an operation: ")
        second_num = float(input("What's the second number?: "))


        # Conditions to do operation calculation
        results = calculations_check(first_num, second_num)

        choice = input(f"Type 'y' to continue calculating with {results}, "
              "or type 'n' to end the calculation: ")

        if choice == 'y':
            first_num = results
        else:
            should_continue = False
            done = True
