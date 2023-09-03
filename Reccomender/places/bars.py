import requests
import json
from flask import Flask, jsonify
import api_keys
from overview import get_overview

#app = Flask(__name__)

# Places API key, global variable
api_key = api_keys.places


def get_bars(coordinates, desired_price, radius):
    location = coordinates
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=bar&key={api_key}"
    
    
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        bars = data["results"]
        name_price_dict = {}
        for bar in bars:
            # name = bar.get("name", "N/A")
            # price_band = bar.get("price_level", "N/A")
            # name_price_dict[name] = price_band
            name_place_tuple = ((bar.get("name","N/A")) , (bar.get("place_id","N/A")))
            price_band = bar.get("price_level", "N/A")
            name_price_dict[name_place_tuple] = price_band
    else:
        print(f"Request failed with status code {response.status_code}")


    preference_output = {}
    for key, value in name_price_dict.items():
        if value == desired_price:
            place_overview = get_overview(key[1])
            preference_output[place_overview] = key[0]
    
    if not preference_output:
        preference_output = {'No Places':'No Places'}
    
    return preference_output 

