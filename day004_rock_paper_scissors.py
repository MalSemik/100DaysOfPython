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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def print_choice(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)


player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "))
print_choice(player_choice)
computer_choice = random.randint(0, 2)
print("Computer chose:")
print_choice(computer_choice)
if player_choice == computer_choice:
    print("It's a draw")
elif (player_choice == 0 and computer_choice == 1) \
    or (player_choice == 1 and computer_choice == 2) \
    or (player_choice == 2 and computer_choice == 0):
    print("You loose")
else:
    print("You win!")
