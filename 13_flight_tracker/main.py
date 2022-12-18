from datetime import datetime, timedelta
from typing import Any

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destinations()
notification_manager = NotificationManager()
flight_data = FlightData()

ORIGIN_CITY_IATA = 'BCN'
FLIGHT_DATA: dict[Any, Any] = flight_data.data

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destinations = sheet_data
    data_manager.update_destination_codes()

two_months_from_now = (datetime.now() + timedelta(days=60)).strftime("%d/%m/%Y")
one_year_from_today = (datetime.now() + timedelta(days=360)).strftime("%d/%m/%Y")

for destination in sheet_data:
    data = flight_search.get_flight_prices(
        origin=ORIGIN_CITY_IATA,
        destination=destination["iataCode"],
        date_from=two_months_from_now,
        date_to=one_year_from_today,
        max_price=destination['lowestPrice']
    )
    if data:
        data = {data['destination_city']: data}
        FLIGHT_DATA.update(data)

notification_manager.send_email(FLIGHT_DATA)
