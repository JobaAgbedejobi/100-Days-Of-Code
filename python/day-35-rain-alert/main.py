import requests
import smtplib
import os

#TWILIO DIDN'T WORK SO USED EMAIL INSTEAD

user = "os.environ.get("MY_EMAIL")"
EMAIL = os.environ.get("MY_EMAIL")
PASS = os.environ.get("EMAIL_PASSWORD")

#api_key = os.environ.get("OWM_API_KEY")
api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

london_params = {
    "lat": 51.5,
    "lon": 0.0339,
    "appid": api_key,
    "cnt": 4,
}

# stuttgart_params = { # To check code as currently raining here,
# it was raining here when I did today's project
#     "lat": 48.775845,
#     "lon": 9.182932,
#     "appid": api_key,
#     "cnt": 4
# }

response = requests.get(url=OWM_Endpoint, params= london_params)
response.raise_for_status()
weather_data = response.json()

raining = False
for hourly_data in weather_data["list"]:
    condition_codes = (hourly_data["weather"][0]["id"])
    if int(condition_codes) < 700:
        raining = True
if raining:
    print(f"Bring an umbrella!")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=user,
                        msg="It's going to rain later. Bring an umbrella")

# # Environment Variables and hiding API Keys
# Use cases:
# 1. Convenience - When dealing with large amounts of code, could be easier to adjust the variables wihtout directly touching the code
# 2. Security - Not a good idea to store authentication/ API keys in the same location as your code.
# Environment Variables allows you to store your keys and other variables away from your codebase is located (like separating recycling from general rubbish)
# How to create an Environment Variable:
# 1. import os
# 2. Go to terminal
# 3. Type 'export' followed by the name of the variable
# 4. Make sure there's no space between the variable and the '=' sign
# 5. Type the string that the variable equates to
# 6. Once you've exported it, type 'env' and you should see the exported variable
# 7. You can now tap into the environment variable in any of the code that you run in that particular environment
# Set OWM_API_KEY as environment variable

# Includes Date and Time of when it Rains
# condition_codes = []
# tor = []
# raining = False
# for code in range(4):
#     weather_id = weather_data["list"][code]["weather"][0]["id"]
#     condition_codes.append(weather_id)
#     #print(weather_data["list"][code]["dt_txt"])
#     if weather_id < 700:
#         raining = True
#         time_of_rain = weather_data["list"][code]["dt_txt"]
#         print(f"code for TOR: {code}")
#         tor.append(time_of_rain)
# if raining:
#     print(f"Bring an umbrella!\nRaining: {tor}")

