import os
import requests
from dotenv import load_dotenv

load_dotenv()
CITY_SEARCH_ENDPOINT = ("https://test.api.amadeus.com/v1/reference-data/"
                        "locations/cities")
FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
AMADEUS_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.amadeus_api_key = os.environ["AMADEUS_API_KEY"]
        self.amadeus_api_secret = os.environ["AMADEUS_API_SECRET"]
        self._amadeus_token = self._get_new_token()

    def _get_new_token(self):

        header = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_api_key,   # CHANGE DEPENDING ON HEADERS KEY
            "client_secret": self.amadeus_api_secret,
        }
        response = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=header,
                                 data=body)
        print(f"Your Response Token is: {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]


    def get_destination_codes(self,city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.
        Parameters:
        city_name (str): The name of the city for which to find the IATA code.
        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is
        found due to an IndexError, or "Not Found" if no match is found due to a
        KeyError.

        The function sends a GET request to the IATA_ENDPOINT with a query that
        specifies the city name and other parameters to refine the search. It then
        attempts to extract the IATA code from the JSON response.
        - If the city is not found in the response data (i.e., the data array is empty,
        leading to an IndexError), it logs a message indicating that no airport code
        was found for the city and returns "N/A".
        - If the expected key is not found in the response (i.e., the 'iataCode' key is
        missing, leading to a KeyError), it logs a message indicating that no airport
        code was found for the city and returns "Not Found".
        """
        city_params = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS",
        }
        headers = {
            "Authorization": f"Bearer {self._amadeus_token}",
        }
        # print(f"Using this token to get destination: {self._amadeus_token}")
        response = requests.get(url=CITY_SEARCH_ENDPOINT, params=city_params,
                                headers=headers)

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            iatacode = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return iatacode

    def check_flights(self,to_city,from_time,to_time, is_direct=True):
        """
        Searches for flight options between two cities on specified departure and
        return dates
        using the Amadeus API.
        Parameters:
            origin_city_code (str): The IATA code of the departure city (London).
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.
        Returns:
            dict or None: A dictionary containing flight offer data if the query is
             successful; None
            if there is an error.
        The function constructs a query with the flight search parameters and sends a
        GET request to the API. It handles the response, checking the status code
        and parsing the JSON data if the request is successful. If the response status
        code is not 200, it logs an error message and provides a link to the API
        documentation for status code details. :param to_city:
        """

        # print(f"Using this token to check_flights(): {self._amadeus_token}")
        flight_params = {
            "originLocationCode": "LON",
            "destinationLocationCode": to_city,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10
        }
        header = {
            "Authorization": f"Bearer {self._amadeus_token}",
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=header,
                                params=flight_params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/"
                  "api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()