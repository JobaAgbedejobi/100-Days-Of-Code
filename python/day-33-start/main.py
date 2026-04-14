# An Application Programming Interface (API) is a set of commands, functions,
# protocols and objects that programmers can use to create software or interacts with
# an external system.

# API Endpoints and making API calls

import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
#
# # Response codes (x represents a digit e.g. 1XX could be 173, 2XX could be 284 etc):
# # 1XX: Hold On - Something's happening, this isn't final
# # 2XX: Here you go - Everything went as expected
# # 3XX: Go Away - You don't have permission
# # 4XX: You screwed up - What your looking for may not exist e.g 404
# # 5XX: I screwed up - The server screwed up, maybe it or the website's down
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

MY_LAT = 51.507351
MY_LNG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)