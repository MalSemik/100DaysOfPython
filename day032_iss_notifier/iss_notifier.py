import time
import smtplib
import requests
import datetime as dt


MY_LAT = 49.854850
MY_LONG = 19.338540


def is_iss_near():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = iss_latitude - MY_LAT
    long_diff = iss_longitude - MY_LONG
    if abs(lat_diff) <= 5 and abs(long_diff) <= 5:
        return True


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now()
    current_hour = time_now.hour
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True


def send_email():
    my_email = "magija.crochet@gmail.com"
    password = "fgydkxytijgpxslw"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="malg.sem@gmail.com",
            msg=f"Subject:Look up!\n\n The ISS should be visible in your area."
        )


while True:
    if is_iss_near() and is_nighttime():
        send_email()
    time.sleep(60)
