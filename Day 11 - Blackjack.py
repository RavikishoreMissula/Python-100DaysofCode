import random

def blackjack():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_cards = []
    computer_cards = []
    player_total = 0
    computer_total = 0

    for a in range(2):
        player_card = random.choice(cards)
        player_cards.append(player_card)
        player_total += player_card
        computer_card = random.choice(cards)
        computer_cards.append(computer_card)
        computer_total += computer_card

    continue_player_game = True
    continue_computer_game = True

    while continue_player_game:
        if player_total == 21 and computer_total == 21:
            print(f"Your Cards: {player_cards}, Current Score: {player_total}")
            print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
            print('Its a Draw!')
            continue_player_game = False
            continue_computer_game = False
        elif player_total == 21 and computer_total < 21:
            print(f"Your Cards: {player_cards}, Current Score: {player_total}")
            print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
            print('Its a Blackjack! You Win!')
            continue_player_game = False
            continue_computer_game = False
        elif player_total < 21:
            print(f"Your Cards: {player_cards}, Current Score: {player_total}")
            print(f"Computer's first card is: {computer_cards[0]}")
            player_new_card = input("Type 'y' to get another card or Type 'n' to pass: ").lower()
            if player_new_card == 'y':
                player_card = random.choice(cards)
                player_cards.append(player_card)
                player_total += player_card
                if player_total > 21 and (11 in player_cards):
                    player_cards[player_cards.index(11)] = 1
                    player_total -= 10
            else :
                continue_player_game = False
        elif player_total > 21:
            print(f"Your Cards: {player_cards}, Current Score: {player_total}")
            print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
            print('You Went Over! You Lose!')
            continue_player_game = False
            continue_computer_game = False

    while continue_computer_game:
        if computer_total > 21:
            print(f"Your Cards: {player_cards}, Current Score: {player_total}")
            print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
            print('Computer Went Over! You Win!')
            continue_computer_game = False
        elif computer_total >= 17:
            if computer_total > player_total:
                print(f"Your Cards: {player_cards}, Current Score: {player_total}")
                print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
                print('Computer has higher score! You Lose!')
                continue_computer_game = False
            elif computer_total < player_total:
                print(f"Your Cards: {player_cards}, Current Score: {player_total}")
                print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
                print('You have higher score! You Win!')
                continue_computer_game = False
            else :
                print(f"Your Cards: {player_cards}, Current Score: {player_total}")
                print(f"Computer's Cards: {computer_cards}, Compute Score: {computer_total}")
                print("You have same score! It's a Draw!")
                continue_computer_game = False
        elif computer_total <= 16:
            computer_card = random.choice(cards)
            computer_cards.append(computer_card)
            computer_total += computer_card
            if computer_total > 21 and (11 in computer_cards):
                computer_cards[computer_cards.index(11)] = 1
                computer_total -= 10

wanna_play = True
while wanna_play:
    answer = input("Do you want to play the game of Blackjack? Type 'Y' or 'N' ").lower()
    if answer == 'y':
        blackjack()
    elif answer == 'n':
        wanna_play = False
    else :
        print("Invalid Option.Please try Again!")