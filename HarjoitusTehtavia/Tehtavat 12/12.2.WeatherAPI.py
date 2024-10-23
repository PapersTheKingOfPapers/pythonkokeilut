import json
import os
import requests

api_key = json.loads('weatherApiKey.json')["apiKey"]

geocodeapi = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country_code}&limit=1&appid={api_key}"
weatherapi = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
