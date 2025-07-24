# HTTP Requests Library

## Overview
This project demonstrates the use of Python's `requests` library for HTTP operations and API interactions. It includes examples of making HTTP requests, handling responses, and implementing efficient API interactions with caching mechanisms.

## Features
- Basic HTTP GET requests to various websites
- Response status code checking and content extraction
- URL parameter handling for search queries
- JSON response parsing
- Weather data API integration
- Implementation of a Time-To-Live (TTL) caching system for API requests
- Error handling for API requests

## Components

### Basic HTTP Requests Demo
The `http_requests_demo.py` file demonstrates:
- Making simple GET requests to websites
- Checking response status codes
- Accessing response content, headers, and encoding
- Using query parameters for search functionality
- Handling JSON responses

### Weather API with TTL Cache
The `weather_data_api_with_ttl_cache.py` file implements:
- A caching system with expiration time for API responses
- OpenWeatherMap API integration
- Structured data parsing from JSON responses
- Efficient API usage by avoiding redundant requests

### Weather API with UI
The `weather_data_api_ttl_cache_UI.py` file extends the caching implementation with a user interface for weather data retrieval.

## How It Works
1. The program makes HTTP requests to various endpoints using the `requests` library
2. For API requests, it first checks if the requested data is in the cache and not expired
3. If valid cached data exists, it returns that data without making a new API request
4. If no valid cache exists, it makes a new API request and stores the response in the cache
5. The cache includes a timestamp to track when data was last fetched
6. Data is automatically refreshed when the cache expires (default: 30 minutes)

## Usage Example
```python
# Example from weather_data_api_with_ttl_cache.py
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
city_name = "New York"

# First request - fetches from API
weather_json = get_weather_data(city_name, API_KEY)
weather_info = parse_weather_data(weather_json)
print(weather_info)
# Output: Fetched new data for: New York
# {'City': 'New York', 'Temperature (°C)': 22.5, 'Humidity (%)': 65, 'Weather Condition': 'Partly cloudy', 'Wind Speed (m/s)': 3.6}

# Second request within cache expiry time - returns cached data
weather_json = get_weather_data(city_name, API_KEY)
weather_info = parse_weather_data(weather_json)
print(weather_info)
# Output: Returning cached data for: New York
# {'City': 'New York', 'Temperature (°C)': 22.5, 'Humidity (%)': 65, 'Weather Condition': 'Partly cloudy', 'Wind Speed (m/s)': 3.6}
```

## Skills Demonstrated
- HTTP request handling with the `requests` library
- API integration and authentication
- JSON data parsing
- Caching implementation for performance optimization
- Time-based cache expiration
- Error handling for network operations
- Data extraction and formatting

## Requirements
- Python 3.6 or higher
- `requests` library (`pip install requests`)
- OpenWeatherMap API key (for weather data examples)