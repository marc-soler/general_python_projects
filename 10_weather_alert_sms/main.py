import os
import requests
from twilio.rest import Client

ACCOUNT_SID = os.environ['ACCOUNT_SID']
OWM_API_KEY = os.environ['OWM_API_KEY']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
client = Client(ACCOUNT_SID, AUTH_TOKEN)
sender = '+19049068867'
phone = '+34650718618'
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "appid": OWM_API_KEY,
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
