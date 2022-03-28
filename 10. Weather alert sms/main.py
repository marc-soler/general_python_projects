import os
import requests
from twilio.rest import Client

os.environ['ACCOUNT_SID'] = 'AC1fa2c440d9d4ef77ad18a250e4552f70'
os.environ['OWM_API_KEY'] = 'f9c3012a8ed831096469d511ac13e286'
os.environ['AUTH_TOKEN'] = 'de139c7668842bc995a0c5df6993b869'
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)
sender = '+19049068867'
phone = '+34650718618'
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("OWM_API_KEY")
weather_params = {
    "appid": api_key,
    "lat": 41.385063,
    "lon": 2.173404,
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
for hour in data['hourly'][:12]:
    if hour['weather'][0]['id'] < 700:
        message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☂️",
                     from_=sender,
                     to=phone
                 )
        break

print(message.status)
