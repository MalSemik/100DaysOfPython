import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = list(string.ascii_letters)
SYMBOLS = list(string.punctuation)
NUMBERS = list(string.digits)


def generate_password():
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    chosen_letters = [random.choice(LETTERS) for i in range(num_letters)]
    chosen_symbols = [random.choice(SYMBOLS) for j in range(num_symbols)]
    chosen_numbers = [random.choice(NUMBERS) for k in range(num_numbers)]
    all_characters = chosen_letters + chosen_symbols + chosen_numbers
    random.shuffle(all_characters)
    password = "".join(all_characters)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Some fields were left empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website}|{email}|{password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# create labels
website_label = Label(text="Website:")
email_label = Label(text="Email/ Username:")
password_label = Label(text="Password:")

# create entries
website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "malg.sem@gmail.com")
password_entry = Entry(width=21)

# create buttons
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_password, width=36)

# create layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

