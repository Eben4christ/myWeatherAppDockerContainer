# from dotenv import load_dotenv
# from pprint import pprint
# import requests
# import os
#
# load_dotenv()
#
#
# def get_current_weather(city="Charlottetown"):
#
#     request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
#
#     weather_data = requests.get(request_url).json()
#
#     return weather_data
#
#
# if __name__ == "__main__":
#     print('\n*** Get Current Weather Conditions ***\n')
#
#     city = input("\nPlease enter a city name: ")
#
#     # Check for empty strings or string with only spaces
#     # This step is not required here
#     if not bool(city.strip()):
#         city = "Charlottetown"
#
#     weather_data = get_current_weather(city)
#
#     print("\n")
#     pprint(weather_data)
#


from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Charlottetown"):
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY not found. Check your .env file.")
        return {}

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric'

    response = requests.get(request_url)

    try:
        # Check if the response was successful
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.JSONDecodeError:
        print("Error: Received invalid JSON response")
        print("Response content:", response.text)  # Shows the raw content returned from the API

    return {}


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    if not city.strip():  # Check for empty input
        city = "Charlottetown"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
