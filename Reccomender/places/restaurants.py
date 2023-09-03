import requests
import json
from flask import Flask, jsonify
import api_keys
from overview import get_overview


# Places API key, global variable
api_key = api_keys.places

#coordinates must be in "lat,long" format

def get_restaurants(coordinates, desired_price,radius):
    location = coordinates

    # google places API used here
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=restaurant&key={api_key}"

    # Make the google API request
    response = requests.get(url)

    # Check if the request was successful and create restaurant price dictionary
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Get the list of restaurants
        restaurants = data["results"]

        # create a dict to store restaurants and price bands
        name_price_dict = {}
        for restaurant in restaurants:
            name_place_tuple = ((restaurant.get("name","N/A")) , (restaurant.get("place_id","N/A")))
            price_band = restaurant.get("price_level", "N/A")
            name_price_dict[name_place_tuple] = price_band

    else:
        # Handle the error
        print(f"Request failed with status code {response.status_code}")

    preference_output = {}
    for key, value in name_price_dict.items():
        if value == desired_price:
            restaurant_overview = get_overview(key[1])
            #preference_output[key[0]] = restaurant_overview
            preference_output[restaurant_overview] = key[0]
            #preference_output.append([key[0],restaurant_overview])
    
    if not preference_output:
        preference_output = {'No restaurants':'No restaurants'}

    return preference_output
    #returns a dict where every item contains name:full_overview



