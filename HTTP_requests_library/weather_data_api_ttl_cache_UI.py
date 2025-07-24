import requests
import time
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import dotenv
import os

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
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
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
    Parses the weather JSON data to extract relevant daily details.
    """
    if not weather_json:
        return None

    daily_forecast = {}

    for item in weather_json["list"]:
        date = item["dt_txt"].split()[0]  # Extract the date (YYYY-MM-DD)
        time = item["dt_txt"].split()[1]  # Extract the time (HH:MM:SS)

        # Select only one record per day, prioritizing the 12:00 PM timestamp
        if date not in daily_forecast or time == "12:00:00":
            daily_forecast[date] = {
                "Date": date,
                "Temperature (°C)": item["main"]["temp"],
                "Humidity (%)": item["main"]["humidity"],
                "Weather Condition": item["weather"][0]["description"].capitalize(),
                "Wind Speed (m/s)": item["wind"]["speed"]
            }

    return list(daily_forecast.values())  # Convert dictionary to list of forecasts


def display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    weather_json = get_weather_data(city, API_KEY)
    weather_info = parse_weather_data(weather_json)

    if weather_info:
        forecast_list.delete(*forecast_list.get_children())
        dates = []
        temperatures = []

        for data in weather_info[:7]:  # Display only 7-day forecast
            forecast_list.insert("", "end", values=(data["Date"], data["Temperature (°C)"], data["Weather Condition"]))
            dates.append(data["Date"])
            temperatures.append(data["Temperature (°C)"])

        plot_chart(dates, temperatures)


def plot_chart(dates, temperatures):
    ax.clear()
    ax.plot(dates, temperatures, marker='o', linestyle='-', color='b')
    ax.set_title("Temperature Trends")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)
    canvas.draw()


# GUI Setup
root = tk.Tk()
root.title("Weather Forecast")

load_dotenv()

API_KEY = os.environ.get("Open_Weather_API_Key")

if not API_KEY:
    # print("Missing API Key. Check your .env file.")
    raise KeyError("Missing API Key. Check your .env file.")
# else:
#     print(f"Debugging API Key: {API_KEY[:5]}...{API_KEY[-5:]}")  # ✅ Safe

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack()
tk.Button(root, text="Get Forecast", command=display_weather).pack()

columns = ("Date", "Temperature (°C)", "Weather Condition")
forecast_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    forecast_list.heading(col, text=col)
forecast_list.pack()

# Matplotlib Figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
