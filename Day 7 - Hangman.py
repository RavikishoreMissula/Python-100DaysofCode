import random
from Hangman_words import word_list
from Hangman_art import stages, logo
print("\nWelcome")
print(logo)

word_to_guess = random.choice(word_list).lower()
guessed_word = []
for letter in word_to_guess:
    guessed_word += '_'

game_over = False
no_of_lives = 6

while not game_over:
    print(f'Word to guess: {"".join(guessed_word)}')
    print(f'************** Lives left: {no_of_lives}/6 **************')
    guessed_letter = input("Enter a letter: ").lower()
    position = 0
    for letter in word_to_guess:
        if letter == guessed_letter:
            guessed_word[position] = letter
        position += 1
    print("".join(guessed_word))

    if guessed_letter not in word_to_guess:
        no_of_lives -= 1
        print(f'You guessed {guessed_letter}, that\'s not in the word. You lose a life.')

    print(stages[no_of_lives])

    if "".join(guessed_word) == word_to_guess:
        game_over = True
        print(f"************** It was {word_to_guess}. You Win! **************")
    elif no_of_lives == 0 :
        game_over = True
        print(f"************** It was {word_to_guess}. You Lose! **************")