import random

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
word_to_guess = random.choice(word_list)
guessed_letters = []
mistake_counter = 0


def print_word(word_to_guess, guessed_letters):
    display = []
    for letter in word_to_guess:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    print(" ".join(display))


while set(guessed_letters) != set(word_to_guess):
    print_word(word_to_guess, guessed_letters)
    guess = input("Guess a letter: ")
    if guess in set(word_to_guess):
        guessed_letters.append(guess)
    else:
        mistake_counter -= 1
        print(stages[mistake_counter])
    if mistake_counter == -7:
        print("You loose!")
        break
    if set(guessed_letters) == set(word_to_guess):
        print_word(word_to_guess, guessed_letters)
        print("You win!")
