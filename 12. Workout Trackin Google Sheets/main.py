import requests as re
from datetime import datetime
import os

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
URL_SHEETY = os.environ["SHEET_ENDPOINT"]
NOW = datetime.now()

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
exercise = {
    "query": str(input('Which exercises did you do? ')),
    "gender": "male",
    "weight_kg": 90.5,
    "height_cm": 188,
    "age": 24
}

response = re.post(url=URL, headers=headers, json=exercise)
result = response.json()['exercises']

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

for exercise in result:
    sheets = {
        'workout': {
            'date': NOW.strftime('%d/%m/%Y'),
            'time': NOW.strftime("%X"),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    write_sheets = re.post(url=URL_SHEETY, json=sheets, headers=bearer_headers)
