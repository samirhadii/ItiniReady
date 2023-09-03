from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
import api_keys


def get_coords(street, city, state, zipcode):

    auth_id = api_keys.smarty_auth_id
    auth_token = api_keys.smarty_auth_token

    credentials = StaticCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_street_api_client()

    lookup = StreetLookup()
    lookup.addressee = "John Doe"
    lookup.street = street
    lookup.city = city
    lookup.state = state
    lookup.zipcode = zipcode

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        print("No candidates. This means the address is not valid.")
        return

    first_candidate = result[0]

    latitude = format(first_candidate.metadata.latitude)
    longitude = format(first_candidate.metadata.longitude)
    latlong = str(latitude+","+longitude)

    return latlong


