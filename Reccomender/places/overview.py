import requests
import api_keys
import json
#USE JSON LOADS TO TURN JSON DATA TO DICT

#takes in the places_id as a string
def get_overview(place_id):
    api_key = api_keys.places

    # Send a GET request to the Place Details API endpoint
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Ceditorial_summary&key={api_key}"
    response = requests.get(url)

    # Extract the PlaceEditorialSummary from the response if the response is ok 
    if response.status_code == 200:
        data = json.loads(response.text)
        #store the value of the json result
        result = data["result"]
        name = result.get("name","N/A")
        #dictionary that has langauge and overview stored in it
        editorial_summary = result.get("editorial_summary","N/A")
        #check the type of editorial summary if it exists to dodge errors of trying to find the value of a string
        if type(editorial_summary) is dict:
            overview = editorial_summary.get("overview","N/A")
        else:
            overview = "N/A"
        
        full_overview = name + ": " + overview

    else:
        print(f"Request failed with status code {response.status_code}")
        full_overview = "None"
    
    return full_overview #will return overview as a string

#print(get_overview("ChIJfVDbwmYE9YgR8I_45Rl2taA"))