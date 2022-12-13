import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK = "TSLA"
COMPANY = "Tesla Inc"
STOCK_API = os.environ["STOCK_API"]
NEWS_API = os.environ['NEWS_API']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
ACCOUNT_SID = os.environ['ACCOUNT_SID']


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API}'
r = requests.get(url)
data = r.json()

def get_date():
    td = datetime.today().weekday()
    if td == 0:
        yt = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
        db = datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d')
    elif td == 1:
        yt = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        db = datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d')
    elif td == 6:
        yt = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
        db = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
    else:
        yt = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        db = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
    return (yt, db)

date = get_date()
yesterday = date[0]
day_before = date[1]
yesterday_price = data['Time Series (Daily)'][yesterday]['4. close']
day_before_price = data['Time Series (Daily)'][day_before]['4. close']
prc = float(yesterday_price) / float(day_before_price)
if prc >= 1.05 or prc <= 0.95:
    url = f'https://newsapi.org/v2/everything?q={COMPANY}&from={get_date()[0]}&sortBy=popularity&apiKey={NEWS_API}'
    data = requests.get(url).json()['articles'][:3]

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
client = Client(ACCOUNT_SID, AUTH_TOKEN)
sender = '+19049068867'
phone = '+34650718618'
for article in data:
    if prc > 1:
        message = client.messages \
                        .create(
                             body=f"""
                             TSLA: {prc}% 🔺
                             Headline: {article['title']}\n
                             Brief: {article['content']}\n
                             url: {article['url']}
                             """,
                             from_=sender,
                             to=phone
                         )
    else:
        message = client.messages \
                        .create(
                             body=f"""
                             TSLA: {prc}% 🔻
                             Headline: {article['title']}\n
                             Brief: {article['content']}\n
                             url: {article['url']}
                             """,
                             from_=sender,
                             to=phone
                         )
    print(message.status)