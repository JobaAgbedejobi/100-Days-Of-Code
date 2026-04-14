from pprint import pprint
class FlightData:
#This class is responsible for structuring the flight data.
    def __init__(self, price, from_airport, to_airport, out_date, return_date, stops):
        self.price = price
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def cheapest_flights(data):
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight
    option among multiple entries.
    Args:
        data (dict): The JSON data containing flight information returned by the API.
    Returns:
        FlightData: An instance of the FlightData class representing the cheapest
        flight found, or a FlightData instance where all fields are 'NA' if no valid
        flight data is available.

    This function initially checks if the data contains valid flight entries. If no
    valid data is found, it returns a FlightData object containing "N/A" for all
    fields. Otherwise, it starts by assuming the first flight in the list is the
    cheapest. It then iterates through all available flights in the data, updating
    the cheapest flight details whenever a lower-priced flight is encountered. The
    result is a populated FlightData object with the details of the most affordable
    flight.
    """

    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data["data"]:
        print("No Data for Flights")
        return FlightData("N/A", "N/A", "N/A",
                          "N/A", "N/A", "N/A")


    # Initialize FlightData with the first flight for comparison
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    from_airport = (first_flight["itineraries"][0]["segments"][0]["departure"]
    ["iataCode"])
    to_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = (first_flight["itineraries"][0]["segments"][0]["departure"]
    ["at"]).split("T")[0]
    return_date = (first_flight["itineraries"][1]["segments"][0]["departure"]
    ["at"]).split("T")[0]
    cheapest_flight = FlightData(price=lowest_price, from_airport=from_airport,
                                 to_airport=to_airport, out_date=out_date,
                                 return_date=return_date, stops=1)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = float(flight["price"]["grandTotal"])
            from_airport = (flight["itineraries"][0]["segments"][0]["departure"]
            ["iataCode"])
            to_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = (flight["itineraries"][0]["segments"][0]["departure"]
            ["at"]).split("T")[0]
            return_date = (flight["itineraries"][1]["segments"][0]["departure"]
            ["at"]).split("T")[0]
            # stops = len(flight["itineraries"])
            cheapest_flight = FlightData(lowest_price, from_airport, to_airport,
                                         out_date, return_date)
            print(f"The cheapest flight for {to_airport} is £{lowest_price}")
    pprint(first_flight)
    return cheapest_flight