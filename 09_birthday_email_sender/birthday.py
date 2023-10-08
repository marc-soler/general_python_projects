import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "praisedbethelord69@gmail.com"
password = "Thisisadummyaccount69"
now = dt.datetime.now()
current_date = (now.month, now.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if current_date in birthdays_dict:
    birthday_name = birthdays_dict[current_date]["name"]
    birthday_email = birthdays_dict[current_date]["email"]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, 'r') as letter:
        contents = letter.read()
        final_text = contents.replace("[NAME]", f"{birthday_name}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{birthday_email}",
            msg=f'Subject: Happy birthday!\n\n{final_text}'
        )
