import requests as re
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "vUojMjD7bRWle2BDboZ2EfKvPIAN_DXI"


class FlightSearch:
    def get_destination_code(self, city_name):
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = re.get(url=endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    def get_flight_prices(self, origin, destination, date_from, date_to, max_price):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        min_nights = 4 if max_price > 200 else 2
        max_nights = 20 if max_price > 200 else 4
        query = {"fly_from": origin,
                 "fly_to": destination,
                 "date_from": date_from,
                 "date_to": date_to,
                 "flight_type": "round",
                 "price_to": max_price,
                 "adults": 2,
                 "nights_in_dst_from": min_nights,
                 "nights_in_dst_to": max_nights,
                 "max_stopovers": 2,
                 "one_for_city": 1,
                 "currency": "EUR"}
        response = re.get(url=location_endpoint, headers=headers, params=query)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data

