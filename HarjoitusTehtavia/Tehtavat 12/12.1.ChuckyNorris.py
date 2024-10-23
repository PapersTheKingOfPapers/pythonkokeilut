import requests

api = "https://api.chucknorris.io/jokes/random"
responce = requests.get(api).json()
print(responce["value"])