import random
import smtplib
import datetime as dt


def send_email(quote):
    my_email = "magija.crochet@gmail.com"
    password = "fgydkxytijgpxslw"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="malg.sem@gmail.com",
            msg=f"Subject:Your daily motivational quote\n\n {quote}"
        )


def get_random_quote():
    with open("quotes.txt", "r", encoding="utf8") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        return quote.encode('utf-8')


if dt.datetime.now().weekday() == 3:
    send_email(get_random_quote())

