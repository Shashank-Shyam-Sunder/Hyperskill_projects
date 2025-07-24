import requests


def get_weather_data(api_key, location):
    """
    Retrieve current weather data for a specific location using OpenWeatherMap API.

    Parameters:
    - api_key: str, your API key for OpenWeatherMap
    - location: str, the location (e.g., city name or coordinates) for which
      you want to get the weather information

    Returns:
    - response.json(): dict, the JSON response from the API if the request is successful
    - None: if there is an error with the request
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving weather data: {e}")
        return None

# Example usage:
# api_key = "your_openweathermap_api_key"
# location = "London"
# weather_data = get_weather_data(api_key, location)

def parse_weather_data(data):
    """
    Parse the JSON response from the weather API to extract relevant weather information.

    Parameters:
    - data: dict, the JSON data object returned by the weather API

    Returns:
    - weather_info: dict, containing parsed weather information
    """
    if data is None:
        return None

    try:
        weather_info = {
            'location': data['name'],
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    except KeyError as e:
        print(f"Error parsing data: {e}")
        return None

# Example usage:
# if weather_data:
#     parsed_data = parse_weather_data(weather_data)
#     print(parsed_data)