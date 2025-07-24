import time

class WeatherCache:
    def __init__(self):
        self.cache = {}
        self.ttl = 300  # Time-to-live in seconds (e.g., 5 minutes)

    def get(self, location):
        entry = self.cache.get(location)
        if entry is None:
            return None
        timestamp, data = entry
        if time.time() - timestamp < self.ttl:
            return data
        else:
            # Invalidate the cache entry
            del self.cache[location]
            return None

    def set(self, location, data):
        self.cache[location] = (time.time(), data)


def get_cached_weather_data(api_key, location, cache):
    """
    Retrieve current weather data for a specific location using OpenWeatherMap API
    and cache the results.

    Parameters:
    - api_key: str, your API key for OpenWeatherMap
    - location: str, the location for which you want to get the weather information
    - cache: WeatherCache, the caching mechanism to use

    Returns:
    - weather_data: dict, the weather data either from the cache or fetched from the API
    """
    # Check the cache first
    cached_data = cache.get(location)
    if cached_data:
        print("Returning cached data.")
        return cached_data

    # If not in cache, fetch from the API
    weather_data = get_weather_data(api_key, location)
    if weather_data:
        cache.set(location, weather_data)
    return weather_data

# Example usage:
# weather_cache = WeatherCache()
# api_key = "your_openweathermap_api_key"
# location = "London"
# weather_data = get_cached_weather_data(api_key, location, weather_cache)