import pandas as pd
import datetime as dt
import random
import smtplib

TEMPLATES = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]


def fill_template(name):
    template = random.choice(TEMPLATES)
    with open(template, "r") as t:
        return t.read().replace("[NAME]", name)


def send_email(message):
    my_email = "magija.crochet@gmail.com"
    password = "fgydkxytijgpxslw"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="malg.sem@gmail.com",
            msg=f"Subject:It's your birthday!\n\n {message}"
        )


now = dt.datetime.now()
day = now.day
month = now.month


df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    if row["month"] == month and row["day"] == day:
        send_email(fill_template(row["name"]))
