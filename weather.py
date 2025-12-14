import requests
from datetime import datetime

API_KEY = "7d9ffff60d86a9641c6aebc24762968d"
CITY = "Mumbai"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_data():
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    weather_info = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "is_rainy": 1 if data["weather"][0]["main"] == "Rain" else 0
    }

    return weather_info


if __name__ == "__main__":
    print(get_weather_data())
