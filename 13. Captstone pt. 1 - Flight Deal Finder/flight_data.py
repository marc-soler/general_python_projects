import datetime as dt


class FlightData:
    """This class is responsible for structuring the flight data."""
    
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.departure_time = (dt.datetime.now() + dt.timedelta(days=15)).strftime("%d/%m/%Y")
        self.max_return_date = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")
