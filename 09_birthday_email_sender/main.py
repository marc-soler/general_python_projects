import smtplib
import datetime as dt
import random as rd

my_email = "praisedbethelord69@gmail.com"
password = "Thisisadummyaccount69"
now = dt.datetime.now()
current_weekday = now.weekday()


if current_weekday == 4:
    with open("quotes.txt", "r") as quotes:
        quote = rd.choice(quotes.readlines())

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="msolerjosa@gmail.com",
            msg=f'Subject: Palabra del Senor\n\n{quote}'
        )
