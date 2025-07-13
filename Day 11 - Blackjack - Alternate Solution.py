import random

def deal_card():
    """Returns a random number from the given list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_total(cards):
    """Calculate the sum of element of the list"""
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
        return sum(cards)
    else :
        return sum(cards)

def compare(p_total,c_total):
    """Compare the Player Total and Computer total and show the result"""
    if p_total == c_total:
        print("It's a Draw")
    elif p_total == 21:
        print("You have a Blackjack. You Win!")
    elif c_total == 21:
        print("Computer has a Blackjack. You Lose!")
    elif p_total > 21:
        print("You Went Over. You Lose!")
    elif c_total > 21:
        print("Computer Went Over. You Win!")
    elif p_total > c_total:
        print("You have higher score. You Win!")
    else:
        print("Computer has higher score. You Lose!")

def blackjack():
    """Blackjack game code. using this function to execute game recursively."""
    player_cards = []
    computer_cards = []

    for a in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    continue_player_game = True
    continue_computer_game = True
    player_total = 0
    computer_total = 0

    while continue_player_game:
        player_total = calculate_total(player_cards)
        computer_total = calculate_total(computer_cards)

        print(f"Your Cards: {player_cards}, Current Score: {player_total}")
        print(f"Computer's first Card: {computer_cards[0]}")

        if player_total == 21 or computer_total == 21 or player_total > 21:
            continue_player_game = False
        else :
            player_new_card = input("Type 'y' to get another card or Type 'n' to pass: ").lower()
            if player_new_card == 'y':
                player_cards.append(deal_card())
            else :
                continue_player_game = False

    while continue_computer_game:
        if computer_total > 21:
            continue_computer_game = False
        elif computer_total <= 16:
            computer_cards.append(deal_card())
            computer_total = calculate_total(computer_cards)
        else:
            continue_computer_game = False

    print(f"Your final Cards: {player_cards}, Total Score: {player_total}")
    print(f"Computer final Cards: {computer_cards}, Total Score: {computer_total}")
    compare(player_total,computer_total)

play_game = True
while play_game:
    answer = input("Do you want to play the game of Blackjack? Type 'Y' or 'N': ").lower()
    if answer == 'y':
        blackjack()
    elif answer == 'n':
        play_game = False
    else :
        print("Invalid Option.Please try Again!")