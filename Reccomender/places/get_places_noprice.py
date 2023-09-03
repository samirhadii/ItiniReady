import requests
import json
import api_keys
from overview import get_overview



# Places API key, global variable
api_key = api_keys.places

def get_places_noprice(place_type,coordinates,radius):
    location = coordinates
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}"
    
    response = requests.get(url)


    if response.status_code == 200:
        data = json.loads(response.text)
        places = data["results"]

        preference_output={}
        for place in places:
            name_place_tuple = ((place.get("name","N/A")) , (place.get("place_id","N/A")))
            place_overview = get_overview(name_place_tuple[1])
            preference_output[place_overview] = name_place_tuple[0]

        if not preference_output:
            preference_output = {'No places':'No places'}
    else:
        return(f"Request failed with status code {response.status_code}")

    return preference_output

#print(get_places_noprice("movie_theater","33.879727,-84.034444",5000))
    
