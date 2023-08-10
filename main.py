############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from art import logo
from os import system, name  # For clearing the system terminal


# Building out the clear terminal function
def clear():

    # This is for Windows
    if name == 'nt':
        _ = system('cls')

    # This is for Mac, Linux
    else:
        _ = system('clear')


# Deals on card to designated player
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Checks score of designated player
def check_score(player):
    sum = 0
    for card in player:
        sum += card
    return sum


# Initializes End Game sequence
def end_game(user, computer):
    clear()

    user_score = check_score(user)
    computer_score = check_score(computer)
    
    # Checks for winner/draw
    if (user_score > computer_score) and (user_score < 22):
        print(f"The dealer's score is: {computer_score}")
        print(f"Your score is: {user_score}")
        print("You Win!")
    elif (user_score == computer_score) and (user_score < 22):
        print(f"The dealer's score is: {computer_score}")
        print(f"Your score is: {user_score}")
        print("It's a DRAW!")
    else:
        print("You Lose")

    # Asks if user would like to play again
    play_again = input("Would you like to play again? Type 'y' or 'n':\n")

    if play_again == 'y':
        clear()
        start_game()
    elif play_again == 'n':
        clear()
        print("Thanks for playing!")


# Asks user if they would like another card and deals one appropriately
def hit_me(user, computer):
    wants_hit = input("Would you like another card? Type 'y' or 'n': \n")
    
    if wants_hit == 'y':
        clear()
        user.append(deal_card())
        computer.append(deal_card())
        print(f"The dealer's first card is: {computer[0]}")
        print(f"Your cards are: {user}")
        print(f"Your current score is: {check_score(user)}")
    else:
        end_game(user, computer)
        

# Initialize the game, deal cards, and display scores
def start_game():
    user = []
    computer = []
    user.append(deal_card())
    user.append(deal_card())
    computer.append(deal_card())
    computer.append(deal_card())

    print(f"The dealer's first card is: {computer[0]}")
    print(f"Your cards are: {user}")
    print(f"Your current score is: {check_score(user)}")

    while check_score(user) < 22 :
        hit_me(user, computer)

    end_game(user, computer)


# GAME START
print(logo)

start_input = input("Do you want to start a game? Type 'y' or 'n'\n")
if start_input == 'y':
    clear()
    start_game()