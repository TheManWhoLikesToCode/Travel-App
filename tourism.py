from typing import List, Dict, Any
import requests
from requests.exceptions import RequestException

API_KEY = '5ae2e3f221c38a28845f05b6fabd118a2607fe089a18dc2906b76ddb'

GEONAME_API = 'https://api.opentripmap.com/0.1/en/places/geoname'
RADIUS_API = 'https://api.opentripmap.com/0.1/en/places/radius'

PROXY = 'http://themanwholikestocode.pythonanywhere.com/'
proxies = {'http': PROXY, 'https': PROXY}


def get_geoname_data(destination: str) -> Dict[str, Any]:

    print("Getting geoname data for:", destination)

    params = {'name': destination, 'apikey': API_KEY}

    try:
        response = requests.get(GEONAME_API, params=params, proxies=proxies)
        geoname_data = response.json()
        print("Geoname API response:", geoname_data)
        return geoname_data

    except RequestException as e:
        print("Error getting geoname data:", e)
        return {}


def get_locations_to_explore(destination: str) -> List[Dict[str, Any]]:

    # Input validation
    if not destination:
        print("Destination cannot be empty")
        return []

    if not isinstance(destination, str):
        print("Destination must be a string")
        return []

    # Get geoname data
    geoname_data = get_geoname_data(destination)

    # Extract lat and lon
    lat = geoname_data.get('lat')
    lon = geoname_data.get('lon')

    # Define Radius params
    radius_params = {
        'radius': '5000',
        'lat': lat,
        'lon': lon,
        'kinds': 'interesting_places',
        'apikey': API_KEY
    }

    # Radius API call
    try:
        print("Calling Radius API")
        response = requests.get(
            RADIUS_API, params=radius_params, proxies=proxies)
        radius_data = response.json()

        print("Radius API response:", radius_data)

        if 'error' in radius_data:
            print("Radius API error:", radius_data['error'])
            return []

        if 'features' not in radius_data:
            print("No features found")
            return []

        locations = radius_data['features']
        return locations

    except RequestException as e:
        print("Radius API request failed:", e)
        return []
