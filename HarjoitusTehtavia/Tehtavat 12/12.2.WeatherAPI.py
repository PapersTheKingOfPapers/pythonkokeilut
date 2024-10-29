import json
import requests

'''
Make a file with the name "weatherApiKey.json" in the same folder as this script.
The contents of said file should match the example below, with 'KEY_HERE' being your API key.
{
  "apiKey" : "KEY_HERE"
}
'''

with open('weatherApiKey.json') as f:
    api_key = json.load(f)["apiKey"]

def kelvin_to_celcius(kelvin):
    return round(kelvin - 273.15, 2)

while True:
    city_name = input("Paikkakunnan nimi: ")
    if city_name == "":
        break
    geocodeapi = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    georesponce = requests.get(geocodeapi).json()[0]
    lat = georesponce["lat"]
    lon = georesponce["lon"]
    country = georesponce["country"]
    name = georesponce["name"]
    weatherapi = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    weatherresponce = requests.get(weatherapi).json()
    weather = weatherresponce["weather"][0]
    main = weatherresponce["main"]
    weather_type = weather["main"]
    weather_desc = weather["description"]
    temperature = main["temp"]

    print(f"{name} in {country} has a {weather_desc} with a temperature of {kelvin_to_celcius(temperature)} celcius.")
