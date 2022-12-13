class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self):
        self.data = dict
    
    def append_data(self, amount, destination_city, destination_airport, out_date,
                    return_date, link):
        data_update = {destination_city: {
            "price": amount,
            "destination_airport": destination_airport,
            "departure_date": out_date,
            "return_date": return_date,
            "booking_link": link
        }}
        self.data.update(data_update)
