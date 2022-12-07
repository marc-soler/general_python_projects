import requests as re
import os

URL = "https://api.sheety.co/069fc3e0724f467a0517d9433889aa0b/flightDeals/prices"
headers = {
    "Authorization": f"Bearer kjfbw45pojbe4vev64gre"
}


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.destinations = {}
    
    def get_destinations(self):
        response = re.get(url=URL, headers=headers)
        result = response.json()
        self.destinations = result["prices"]
        return self.destinations
    
    def update_destination_codes(self):
        for city in self.destinations:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = re.put(
                url=f"{URL}/{city['id']}",
                headers=headers,
                json=new_data
            )
            print(response.text)
