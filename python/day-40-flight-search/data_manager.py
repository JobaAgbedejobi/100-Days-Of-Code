import requests
from dotenv import load_dotenv
import os

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    load_dotenv()

    def __init__(self):
        self.user = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.sheety_api_token = os.getenv("SHEETY_API_TOKEN")
        self.destination_data = {}

    def get_destination_data(self):
        self.header = {
            "Authorization": self.sheety_api_token,
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,
                                headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):

        for city in self.destination_data:
            update_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            self.headers = {
                "Authorization": self.sheety_api_token,
                "Content-Type": "application/json",
            }

            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                                    json=update_data, headers=self.headers)

            if response.status_code == 200:
                print(f"Successfully updated row {city['id']} with iataCode"
                      f" '{self.update_destination_codes}'.")
            else:
                print(f"Failed to update row {city['id']}. Status code: "
                      f"{response.status_code}")
                print(response.text)

    def update_lowest_price(self, city, price):
        # Updates the lowest price in Sheety to new lowest price found
        update_data = {
            "price": {
                "lowestPrice (£)": price
            }
        }

        self.headers = {
            "Authorization": self.sheety_api_token,
            "Content-Type": "application/json",
        }

        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                                json=update_data, headers=self.headers)

        if response.status_code == 200:
            print(f"Successfully updated row {city['id']} with Lowest Price"
                  f" '£{price}'.")
        else:
            print(f"Failed to update row {city['id']}. Status code: "
                  f"{response.status_code}")
            print(response.text)