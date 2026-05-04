import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=35.6892&longitude=51.3890&current_weather=true"

r = requests.get(url)
data = r.json()

output = {
    "city": "tehran",
    "temperature": data["current_weather"]["temperature"],
    "windspeed": data["current_weather"]["windspeed"]
}

with open("tehran.json", "w") as f:
    json.dump(output, f, indent=2)

print("weather updated")
