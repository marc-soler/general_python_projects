import datetime as dt

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = {}
        self.departure_city = 'BCN'
        self.currency = 'EUR'
        self.departure_time = dt.datetime.now() + dt.timedelta(days=1)
        self.max_return_date = dt.datetime.now() + dt.timedelta(days=180)

fl = FlightData()
print(fl.max_return_date)