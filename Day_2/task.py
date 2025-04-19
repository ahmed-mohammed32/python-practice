# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip_amount = bill * tip_percent
bill_total = bill + total_tip_amount
total = bill_total / people

print(f"Each person should pay: ${round(total, 2)}")
