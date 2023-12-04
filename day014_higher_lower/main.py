import random
from art import logo, vs
from game_data import data


print(logo)


def choose_and_remove_account(data):
    account = random.choice(data)
    data.remove(account)
    return account


def has_more_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'A'
    else:
        return 'B'


def game(score):
    while len(data) > 2:
        account_a = choose_and_remove_account(data)
        account_b = choose_and_remove_account(data)
        print(f"Compare A: {account_a['name']}, {account_a['description']} from {account_a['country']}")
        print(vs)
        print(f"Against B: {account_b['name']}, {account_b['description']} from {account_b['country']}")
        winner = has_more_followers(account_a, account_b)
        player_guess = input("Who has more followers? Type 'A' or 'B': ")
        if winner == player_guess:
            score += 1
            print(f"Congratulations! Your score is: {score}")
            game(score)
        else:
            print("You loose.")
            print(f"Your final score is: {score}")
            break
        if len(data) < 2:
            print("Sorry, we don't have more questions.")
            print(f"Your final score is: {score}")


play_again = ''
while play_again != 'n':
    score = 0
    game(score)
    play_again = input("Do you want to play again? Type 'y' or 'n': ")

