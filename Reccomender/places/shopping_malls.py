import requests
import json
from flask import Flask, jsonify
import api_keys
from overview import get_overview

#app = Flask(__name__)

# Places API key, global variable
api_key = api_keys.places

def get_shopping(coordinates,radius):
    location = coordinates
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=shopping_mall&key={api_key}"
   
  
    response = requests.get(url)


    if response.status_code == 200:
        data = json.loads(response.text)
        shopping_malls = data["results"]

        preference_output={}
        for shopping_mall in shopping_malls:
            name_place_tuple = ((shopping_mall.get("name","N/A")) , (shopping_mall.get("place_id","N/A")))
            place_overview = get_overview(name_place_tuple[1])
            preference_output[place_overview] = name_place_tuple[0]

        if not preference_output:
            preference_output = {'No places':'No places'}
    else:
        return(f"Request failed with status code {response.status_code}")

    return preference_output

#print(get_shopping("33.879727,-84.034444",5000))
    
