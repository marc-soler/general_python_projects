from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destinations()

ORIGIN_CITY_IATA = 'BCN'

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destinations = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.get_flight_prices(
        origin=ORIGIN_CITY_IATA,
        destination=destination["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_today,
        max_price=destination['lowestPrice']
    )
