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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice < 3 :
    print('\nYou choose:\n')
    print(options[user_choice])
else:
    print('Invalid Option. Please try again!')
print('\nComputer choose:\n')
print(options[computer_choice])

if user_choice >= 3 or user_choice < 0 :
    print('Invalid Option. Please try again!')
elif user_choice == computer_choice :
    print('Game Drawn!')
elif user_choice == 0 and computer_choice == 2 :
    print('You Won.')
elif user_choice == 2 and computer_choice == 0 :
    print('You Lose.')
elif user_choice > computer_choice :
    print('You Won.')
elif user_choice < computer_choice :
    print('You Lose.')
else :
    print('Invalid Option. Try Agin!')
