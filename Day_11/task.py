# Blackjack project

import random
from art import logo

# List of cards
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards: []):
    """Return the sum of the list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_sum, comp_sum: int):
    """Compare the user's and computer score"""
    if u_sum == comp_sum:
        return "It's a draw."
    elif comp_sum == 0:
        return "You lose, computer got Blackjack!"
    elif u_sum == 0:
        return "You win, you got Blackjack"
    elif u_sum > 21:
        return "You went over. You lose."
    elif comp_sum > 21:
        return "You win, the computer went over!"
    elif u_sum > comp_sum:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_sum = -1
    user_sum = -1
    is_game_over = False
    # user_cards.append(deal_card())
    # computer_cards.append(deal_card())
    # print(computer_cards)
    # print(user_cards)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # User and computer score
        user_sum = calculate_score(user_cards)
        computer_sum = calculate_score(computer_cards)

        # Show to users cards and sum & 1 of the computer's cards
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            is_game_over = True
        else:
            # Ask if they want another card
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                user_cards.append(deal_card())

            elif another_card == 'n':
                is_game_over = True

            # User and computer score
            user_sum = calculate_score(user_cards)
            computer_sum = calculate_score(computer_cards)

    while computer_sum != 0 and computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_sum}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
    print(compare(user_sum, computer_sum))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 15)
    play_game()
