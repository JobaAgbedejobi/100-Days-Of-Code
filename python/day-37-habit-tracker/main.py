# requests. get() - ask an external system for a particular piece of data, and we
#                   get it back in the response
#          1. post() - we give an external system data and the response is whether
#                    it was successful or not i.e. posting on social media
#          2. put() - update a piece of data in an external system
#          3. delete() - delete a piece of data in an external service

import requests
from datetime import datetime as dt
USERNAME = "jobaa"
TOKEN = os.environ.get("PIXELA_TOKEN")
coding_graph = "graph1"
reading_graph = "graph2"
kickups_graph = "graph3"

GRAPH_ID = coding_graph
colours = ["shibafu", "momiji", "sora", "ichou", "ajisai", "kuro"]
        #   green,      red,     blue,   yellow,  purple,   black   respectively

tracker_dict = {
    coding_graph: ["How many minutes did you code for today? \n", colours[3]],
    reading_graph: ["How many pages did you read today?\n", colours[1]],
    kickups_graph: ["How many Kick Ups did you do today?\n", colours[2]]

}

# 1. POST()
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_config = {
    "id": GRAPH_ID,
    "name": "Kick Ups Graph",
    "unit": "quantity",
    "type": "int",
    "color": tracker_dict[f"{GRAPH_ID}"][1]
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 2. PUT()

# TO AUTOMATE THE UPDATE OF THE DATE:
# date = str(dt.date.today()).split("-")
# DATE = "".join(date)
                # OR:
#today = dt(year=2025, month=7, day=17) # CHANGE DEPENDING ON THE DAY I WANT TO APPEND
today = dt.today()
DATE = today.strftime("%Y%m%d") # '.strftime' formats date into any needed format

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": DATE,
    "quantity": input(tracker_dict[f"{GRAPH_ID}"][0])
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config,
                         headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
update_pixel_config = {
    "quantity": None, # CHANGE TO UPDATE A PIXEL ON A CERTAIN DATE

}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config,
#                         headers=headers)
# print(response.text)

# 3. DELETE()
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)