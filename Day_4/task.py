# Rock, Paper, Scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store Rock, Paper and Scissors in a list & randomize the choices for the computer
rock_paper_or_scissors = [rock, paper, scissors]
computer_choice = random.choice(rock_paper_or_scissors)

# Player's choice stored as a list
player_choice = int(input('"What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors." '))
if player_choice < 0 or player_choice > 3:
    print("You typed an invalid number. You lose.")
choice_of_player_from_list = rock_paper_or_scissors[player_choice]

print(f"You chose: \n {choice_of_player_from_list}")
print("Computer chose: \n" + computer_choice)

# Rock > Scissors, Scissors > Paper, Paper > Rock
if player_choice == 0 and computer_choice == rock_paper_or_scissors[2]:
    print("You Win!")
elif player_choice == 1 and computer_choice == rock_paper_or_scissors[0]:
    print("You Win!")
elif player_choice == 2 and computer_choice == rock_paper_or_scissors[1]:
    print("You Win!")
elif choice_of_player_from_list == rock_paper_or_scissors:
    print("It's a draw!")
else:
    print("You Lose...")
