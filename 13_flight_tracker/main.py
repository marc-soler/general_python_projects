from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destinations()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = 'BCN'

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destinations = sheet_data
    data_manager.update_destination_codes()

two_months_from_now = (datetime.now() + timedelta(days=60)).strftime("%d/%m/%Y")
one_year_from_today = (datetime.now() + timedelta(days=360)).strftime("%d/%m/%Y")

final_data = {}
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
        final_data.update(data)

notification_manager.send_email(final_data)
