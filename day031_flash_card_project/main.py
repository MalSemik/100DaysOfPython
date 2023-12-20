from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
MAIN_FONT = ("Arial", 60, "bold")
SECONDARY_FONT = ("Arial", 40, "italic")

FROM_LANGUAGE = "French"
TO_LANGUAGE = "English"

# Read csv data
df = pd.read_csv("data/french_words.csv")
words_to_learn = df.to_dict(orient="records")


def get_next_flashcard(words_to_learn):
    flashcard = random.choice(words_to_learn)
    print(flashcard)
    word = flashcard[FROM_LANGUAGE]
    print(word)
    translation = flashcard[TO_LANGUAGE]
    print(translation)
    return flashcard, word, translation


def new_word():
    flashcard, word, translation = get_next_flashcard(words_to_learn)
    canvas.itemconfig(card_title, text=FROM_LANGUAGE)
    canvas.itemconfig(card_word, text=word)
    canvas.itemconfig(card_background, image=card_front_img)


def show_translation():
    title = canvas.itemcget(card_title, "text")
    if title == FROM_LANGUAGE:
        canvas.itemconfig(card_title, text=TO_LANGUAGE)
        canvas.itemconfig(card_word, text=translation)
        canvas.itemconfig(card_background, image=card_back_img)
    else:
        canvas.itemconfig(card_title, text=FROM_LANGUAGE)
        canvas.itemconfig(card_word, text=word)
        canvas.itemconfig(card_background, image=card_front_img)


def guessed_right():
    new_word()
    pass
    # learned.append(word)
    # # words.remove(word)
    # new_word()
#
#
# # Create UI
window = Tk()
window.title("Fiszkowo")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard, word, translation = get_next_flashcard(words_to_learn)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text=FROM_LANGUAGE, font=SECONDARY_FONT)
card_word = canvas.create_text(400, 263, text=word, font=MAIN_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas.tag_bind(card_background, '<Button-1>', lambda e: show_translation())
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=sum)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=guessed_right)
known_button.grid(row=1, column=1)

window.mainloop()
