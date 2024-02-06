import requests
import datetime as dt
import os

# TODO: AUTH IDS
NUTRITIONIX_APPLICATION_ID = os.environ["NUTRITIONIX_APPLICATION_ID"]
NUTRITIONIX_APPLICATION_KEY = os.environ["NUTRITIONIX_APPLICATION_KEY"]

SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

# TODO: ENDPOINTS
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT_POST = os.environ["SHEETY_ENDPOINT_POST"]

# TODO: HEADERS
nutritionix_header = {
    "x-app-id": NUTRITIONIX_APPLICATION_ID,
    "x-app-key": NUTRITIONIX_APPLICATION_KEY,
    "x-remote-user-id": "0"
}

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

task = input("what did you do today?: ")

# TODO: DATETIME
now = dt.datetime.now()
date = now.date()
formatted_date = date.strftime("%d/%m/%Y")

time = now.time()
formatted_time = time.strftime("%H:%M:%S")

# TODO: PARAMETERS
nutritionix_parameters = {
    "query": task,
    "gender": "male",
    "weight_kg": 92,
    "height_cm": 190,
    "age": 20
}

# TODO: GETTING NUTRITIONIX JSON
natural_lang = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_parameters, headers=nutritionix_header)
data = natural_lang.json()

duration = str(data["exercises"][0]["duration_min"])
exercise = data["exercises"][0]["name"]
calories = data["exercises"][0]["nf_calories"]

sheety_parameters = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise.title(),
        "duration": f"{duration} min",
        "calories": calories
    }
}

sheety_test = requests.post(url=SHEETY_ENDPOINT_POST, json=sheety_parameters, headers=sheety_header)

