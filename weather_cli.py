import requests


def fetch_weather(city, api_key):

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city,
        "app_id": api_key,
        "units":"metric"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Failed to fetch weather data.")
        print("Status:", response.status_code)
        print(response.text)
        return None

    return response.json()




def display_weather(data):
    if not data:
        return

    city_name = data["name"]
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print(f"City: {city_name}")
    print(f"Temperature: {temperature}")
    print(f"Condition: {description}")


def main():
    api_key = "69721074cdca3736291d1a9577c905ff"
    city = input("Enter city: ")

    data = fetch_weather(city, api_key)
    display_weather(data)
main()