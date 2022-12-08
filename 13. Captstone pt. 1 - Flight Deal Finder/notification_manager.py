import os

from twilio.rest import Client


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
