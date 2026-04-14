import requests
from datetime import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
TOKEN = os.environ.get("TOKEN")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = "https://api.sheety.co"
today = dt.today()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "Authorization": TOKEN,
}

exercise_config = {
    "query": input("What exercises did you do?\n"),
    "gender": "Male",
    "weight_kg": 78,
    "height_cm": 177,
    "age": 22
}

exercise_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_config,
                         headers=headers)
print(exercise_response.text)

EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")
workout_response = exercise_response.json()

for exercise in workout_response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }

    }

    sheet_response = requests.post(url=EXERCISE_ENDPOINT, json=sheet_inputs,
                                   auth=(USER, PASSWORD))
    print(sheet_response.text)

# FIND THE ID OF EACH EXERCISE (IT'S ACTUALLY JUST THE INDEX IN THE GOOGLE SHEET)
# response = requests.get(url=EXERCISE_ENDPOINT, auth=(USER, PASSWORD))
#
# if response.status_code == 200:
#     data = response.json()
#     print("All workout records with IDs:")
#     print("=" * 50)
#
#     for workout in data["workouts"]:  # Note: "workouts" is plural in response
#         print(f"ID: {workout['id']}")
#         print(f"Date: {workout['date']}")
#         print(f"Time: {workout['time']}")
#         print(f"Exercise: {workout['exercise']}")
#         print(f"Duration: {workout['duration']} min")
#         print(f"Calories: {workout['calories']}")
#         print("-" * 30)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)
#
# # DELETE MULLTIPLE EXERCISES BY THEIR IDS
# Delete and verify
# exercise_ids_to_delete = [2, 3, 4]
#
# for exercise_id in exercise_ids_to_delete:
#     delete_url = f"{EXERCISE_ENDPOINT}/{exercise_id}"
#     delete_response = requests.delete(url=delete_url, auth=(USER, PASSWORD))
#
#     if delete_response.status_code == 200:
#         print(f"✅ Successfully deleted exercise ID {exercise_id}")
#
#         # Verify it's actually gone by trying to get it
#         check_response = requests.get(url=delete_url, auth=(USER, PASSWORD))
#         if check_response.status_code == 404:
#             print(f"   ✅ Confirmed: ID {exercise_id} no longer exists")
#         else:
#             print(f"   ⚠️  Warning: ID {exercise_id} might still exist")
#     else:
#         print(f"❌ Failed to delete ID {exercise_id}
#         (Status: {delete_response.status_code})")