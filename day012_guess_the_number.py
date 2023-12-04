import random


print("Welcome to number guessing game!")


def game():
    print(f"I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    difficulty_level = input("Do you want to play easy or hard version? Type 'e' or 'h': ")
    if difficulty_level == 'e':
        lives = 10
    else:
        lives = 5
    while lives > 0:
        guess = int(input("Type your guess: "))
        if guess == number:
            print("You won!")
            break
        else:
            lives -= 1
            if lives == 0:
                print("You loose!")
                break
            if guess > number:
                print("Lower")
            else:
                print("Higher")
            print(f"You have {lives} left.")


play_again = ''
while play_again != 'n':
    game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")