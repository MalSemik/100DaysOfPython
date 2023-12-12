from tkinter import *


def button_clicked():
    new_text = str(round((int(miles_entry.get())*1.609344), 2))
    result_label.config(text=new_text)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)
miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)
equal_label = Label(text="is equal to", font=("Arial", 14))
equal_label.grid(column=0, row=1)
result_label = Label(text="", font=("Arial", 14))
result_label.grid(column=1, row=1)
unit_label = Label(text="Km", font=("Arial", 14))
unit_label.grid(column=2, row=1)
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
