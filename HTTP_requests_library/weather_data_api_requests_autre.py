import requests


def get_weather_data(city, api_key):
    """
    Fetches weather data for a given city using OpenWeatherMap API.

    Args:
        city (str): Name of the city.
        api_key (str): OpenWeatherMap API key.

    Returns:
        dict: Parsed weather information.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data ({response.status_code})")
        return None


def parse_weather_data(weather_json):
    """
    Parses the weather JSON data to extract relevant details.

    Args:
        weather_json (dict): The JSON response from OpenWeatherMap API.

    Returns:
        dict: Extracted weather information.
    """
    if not weather_json:
        return None

    weather_info = {
        "City": weather_json.get("name"),
        "Temperature (°C)": weather_json["main"]["temp"],
        "Humidity (%)": weather_json["main"]["humidity"],
        "Weather Condition": weather_json["weather"][0]["description"].capitalize(),
        "Wind Speed (m/s)": weather_json["wind"]["speed"]
    }

    return weather_info


# Example Usage
if __name__ == "__main__":
    API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
    city_name = "New York"

    weather_json = get_weather_data(city_name, API_KEY)
    weather_info = parse_weather_data(weather_json)

    if weather_info:
        print(weather_info)
