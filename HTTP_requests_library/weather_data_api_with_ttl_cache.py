import requests
import time

# Cache dictionary to store weather data
cache = {}
CACHE_EXPIRY_TIME = 1800  # 30 minutes in seconds


def get_weather_data(city, api_key):
    """
    Fetches weather data for a given city using OpenWeatherMap API with caching.
    """
    current_time = time.time()

    # Check if data is in cache and not expired
    if city in cache:
        cached_data, timestamp = cache[city]
        if current_time - timestamp < CACHE_EXPIRY_TIME:
            print("Returning cached data for:", city)
            return cached_data
        else:
            print("Cache expired for:", city)

    # Fetch new data from API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_json = response.json()
        cache[city] = (weather_json, current_time)  # Store in cache
        print("Fetched new data for:", city)
        return weather_json
    else:
        print(f"Error: Unable to fetch data ({response.status_code})")
        return None


def parse_weather_data(weather_json):
    """
    Parses the weather JSON data to extract relevant details.
    """
    if not weather_json:
        return None

    return {
        "City": weather_json.get("name"),
        "Temperature (°C)": weather_json["main"]["temp"],
        "Humidity (%)": weather_json["main"]["humidity"],
        "Weather Condition": weather_json["weather"][0]["description"].capitalize(),
        "Wind Speed (m/s)": weather_json["wind"]["speed"]
    }


# Example Usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    city_name = "New York"

    weather_json = get_weather_data(city_name, API_KEY)
    weather_info = parse_weather_data(weather_json)

    if weather_info:
        print(weather_info)
