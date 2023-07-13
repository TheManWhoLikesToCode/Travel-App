import requests
from typing import List, Dict, Any

API_KEY = '5ae2e3f221c38a28845f05b6fabd118a2607fe089a18dc2906b76ddb'

GEONAME_API = 'https://api.opentripmap.com/0.1/en/places/geoname'
RADIUS_API = 'https://api.opentripmap.com/0.1/en/places/radius'


def get_locations_to_explore(destination: str) -> List[Dict[str, Any]]:
    """Get interesting locations around a destination."""

    # Input validation
    if not destination:
        print("Destination cannot be empty")
        return []

    if not isinstance(destination, str):
        print("Destination must be a string")
        return []

    # Geoname API
    params = {
        'name': destination,
        'apikey': API_KEY
    }

    try:
        response = requests.get(GEONAME_API, params=params)
        print(response)
        data = response.json()

        destination_lat = data['lat']
        destination_lon = data['lon']

    except requests.exceptions.RequestException as e:
        print(f"Geoname API request failed: {e}")
        return []

    # Radius API
    params = {
        'radius': '5000',
        'lon': destination_lon,
        'lat': destination_lat,
        'kinds': 'interesting_places',
        'apikey': API_KEY,
        'rate': 3,
        'limit': 20
    }

    try:
        response = requests.get(RADIUS_API, params=params)
        data = response.json()

        if 'error' in data:
            print(f"Error from API: {data['error']['message']}")
            return []

        locations = data['features']
        return locations

    except requests.exceptions.RequestException as e:
        print(f"Radius API request failed: {e}")
        return []
