import random
import string


LETTERS = list(string.ascii_letters)
SYMBOLS = list(string.punctuation)
NUMBERS = list(string.digits)

print("Welcome to PyPassword Generator!")
length = int(input("How long would you like your password to be? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like?"))

num_letters = length - num_symbols - num_numbers

chosen_letters = [random.choice(LETTERS) for i in range(num_letters)]
chosen_symbols = [random.choice(SYMBOLS) for i in range(num_symbols)]
chosen_numbers = [random.choice(NUMBERS) for i in range(num_numbers)]
all_characters = chosen_letters + chosen_symbols + chosen_numbers
random.shuffle(all_characters)
password = "".join(all_characters)
print(f"Here is your password suggestion: {password}")
