import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASS = os.environ.get("EMAIL_PASSWORD")
MY_LAT = 51.515049 # Your latitude
MY_LONG = 0.034525 # Your longitude

def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

# STEP 1: If the ISS is close to my current position

    if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG
            <= iss_longitude + 5):
        return True


def at_night() :
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

# STEP 2: and it is currently dark
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True

# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
# STEP 3: Then send me an email to tell me to look up.
    if iss_close() and at_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="LOOK UP! THE ISS IS ABOVE YOU IN THE SKY!")

# # STEP 3: CAN'T DO THIS SO WILL JUST PRINT IT INSTEAD
#     if iss_close() and at_night():
#         print("LOOK UP \n \n THE ISS IS ABOVE YOU!")

