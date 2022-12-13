import os
from twilio.rest import Client
from email.mime.text import MIMEText
from email.header import Header
import smtplib


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    
    def __init__(self):
        self.account_sid = os.environ['TWILIO_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.from_phone = os.environ['TWILIO_PHONE_NUMBER']
        self.to_phone = os.environ['MY_PHONE_NUMBER']
        self.client = Client(self.account_sid, self.auth_token)
    
    def send_sms(self, price, destination_city, destination_airport, out_date, return_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only €{price / 2} per person to fly to {destination_city}-"
                 f"{destination_airport} "
                 f"from {out_date} to {return_date}",
            from_=self.from_phone,
            to=self.to_phone
        )
        return message.sid

    def send_email(self, data):
        text = ""
        for key, value in data.items():
            text_append = f"""
            Flight from Barcelona to {value['destination_city']}({value['destination_airport']}) from €{value['price']}:
            - Departure date: {value['departure_date']}
            - Return date: {value['return_date']}
            - Booking link: {value['booking_link']}
            
            --------------------------------------------
            """
            text += text_append
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.ehlo()
            connection.starttls()
            my_email = os.environ['EMAIL_FROM']
            connection.login(user=my_email, password=os.environ['EMAIL_PASSWORD'])
            msg = MIMEText(text,'plain', 'utf-8')
            msg['From'] = my_email
            msg['To'] = os.environ['EMAIL_TO']
            msg['Subject'] = Header(f'Flight offers', 'utf-8')
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.environ['EMAIL_TO'],
                msg=msg.as_string()
            )
