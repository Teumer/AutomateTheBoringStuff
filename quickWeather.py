#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# quickWeather.py - Prints the weather for a location from the command line

import json
import requests
import sys
from prettytable import PrettyTable
from apikey import *

# Compute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = " ".join(sys.argv[1:])

number_of_days = 3

# Download the JSON data from OpenWeatherMap.org's API
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&cnt={1}&units=imperial&APPID={2}".format(
    location,
    number_of_days,
    apikey
)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weather_data = json.loads(response.text)

# Print weather descriptions
w = weather_data['list']
print("Current weather in {0}: ".format(location))

x = PrettyTable()
x.field_names = ["Day", "Main", "Description", "High", "Morning", "Evening", "Night", "Humidity", "Wind Speed", "Cloudiness"]

for day in range(number_of_days):

    if day == 0:
        dday = "Today"
    elif day == 1:
        dday = "Tomorrow"
    elif day == 2:
        dday = "Day After"
    else:
        dday = "Unknown"

    main = w[day]['weather'][0]['main']
    description = w[day]['weather'][0]['description']
    high = w[day]['temp']['max']
    morn = w[day]['temp']['morn']
    eve = w[day]['temp']['eve']
    night = w[day]['temp']['night']
    humidity = w[day]['humidity']
    speed = w[day]['speed']
    cloud = w[day]['clouds']
    x.add_row([dday, main, description, high, morn, eve, night, humidity, speed, cloud])

print(x)
