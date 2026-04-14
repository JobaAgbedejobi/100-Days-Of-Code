#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import cheapest_flights
from notification_manager import NotificationManager
from pprint import pprint


# --------------------------------------------------------------------------------------

# RAN OUT OF USAGE FOR THIS MONTH (AUG) ON SHEETY SO CAN'T FINISH. MOST RECENT CHANGES
# WERE FROM LINES 34 - 48 (FOR LOOP FOR CHECK_FLIGHTS METHOD)

# --------------------------------------------------------------------------------------


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# pprint(sheet_data)
tomorrow = datetime.now() + timedelta(days=1)
TOMORROW = tomorrow.strftime("%Y-%m-%d")

six_months = tomorrow + timedelta(days=180)
SIX_MONTHS = six_months.strftime("%Y-%m-%d")

# IF I ADD MORE CITIES TO THE GOOGLE SHEET, I NEED TO UNCOMMENT THIS PART
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_codes(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

for destination in sheet_data:
# --------------------------- SEARCHING FOR DIRECT FLIGHTS -----------------------------
    print(f"Getting flights for {destination['city']}...")
    direct_flight = flight_search.check_flights(to_city=destination["iataCode"],
                                          from_time=TOMORROW, to_time=SIX_MONTHS,
                                          is_direct=True)
    cheapest_flight = cheapest_flights(direct_flight)

# -------------------------- SEARCHING FOR INDIRECT FLIGHTS ----------------------------
    if direct_flight is None or not direct_flight.get("data"):
        print(f"No direct flights found for {destination['city']}. "
               "Checking for indirect flights...")
        indirect_flight = flight_search.check_flights(to_city=destination["iataCode"],
                                              from_time=TOMORROW, to_time=SIX_MONTHS,
                                              is_direct=False)

        if indirect_flight is None or not indirect_flight.get("data"):
            print(f"No flights to {destination['city']} - skipping...")
            continue
        cheapest_flight = cheapest_flights(indirect_flight)


    if cheapest_flight.price != "N/A":
        print(f"The cheapest flight to {destination['city']} is "
              f"£{cheapest_flight.price}")
        time.sleep(2)
    if float(cheapest_flight.price) <= float(destination["lowestPrice (£)"]):
        print(f"Lower price to {destination['city']} found!")
#         notification_manager.send_notification(cheapest_flight.price,
#                                                cheapest_flight.from_airport,
#                                                cheapest_flight.to_airport,
#                                                cheapest_flight.out_date,
#                                                cheapest_flight.return_date)
        data_manager.update_lowest_price(destination, cheapest_flight.price)
