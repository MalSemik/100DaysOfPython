import pandas as pd

# df = pd.read_csv("nato_phonetic_alphabet.csv")
# nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
# word_letters = list((input("Enter word to spell: ")).upper())
#
# spelled_letters = [nato_alphabet[letter] for letter in word_letters]
#
# print(spelled_letters)

print([{row.letter: row.code for (index, row) in pd.read_csv("nato_phonetic_alphabet.csv").iterrows()}[letter] for letter in list((input("Enter word to spell: ")).upper())])
