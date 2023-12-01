import os
import operator


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

yes_or_no = ''
bids = {}
while yes_or_no != 'no':
    name = input("What's your name? ")
    bid = input("How much would you like to bid? $")
    bids[name] = int(bid)
    yes_or_no = input("Are there any other bidders? Type \"yes\" or \"no\". ")
    clear_screen()
winner = max(bids.items(), key=operator.itemgetter(1))[0]
print(f"The winner is {winner} with a bid of ${bids[winner]}")
