import random

import hangman_words

stages = ['''
 ------
 |    |
 |    O
 |   /|\
 |   / \
 |
----------
''', '''
 ------
 |    |
 |    O
 |   /|\
 |   /
 |
----------
''', '''
 ------
 |    |
 |    O
 |   /|\
 |
 |
----------
''', '''
 ------
 |    |
 |    O
 |   /|
 |
 |
----------
''', '''
 ------
 |    |
 |    O
 |    |
 |
 |
----------
''', '''
 ------
 |    |
 |    O
 |
 |
 |
----------
''', '''
 ------
 |    |
 |
 |
 |
 |
----------
''']
# word_list = ["ardvark", "baboon", "camel"]
from hangman_words import words_list
chosen_word = random.choice(words_list)
print(f"the chosen word is {chosen_word}")

word_length = len(chosen_word)

lives = 6
display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("guess a letter:\n").lower()

    if guess in display:
        print(f"You have have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"you have guessed {guess}, that's not in the word. you lost a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose!")

    print(f"{' '.join(display)}")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])