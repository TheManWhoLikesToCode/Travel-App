import requests

def get_locations_to_explore(destination):
    api_key = '5ae2e3f221c38a28845f05b6fabd118a2607fe089a18dc2906b76ddb' 

    #URL to request the lat and lon of destination
    url2 = 'https://api.opentripmap.com/0.1/en/places/geoname'

    param1 = {
        'name' : destination,
        'apikey': api_key
    }
    response1 = requests.get(url2, params=param1)
    data1 = response1.json()
    #Stores the lat and lon
    dest_lat = data1['lat']
    dest_lon = data1['lon']

    print("This is the data", data1)
    print("this is lat ", dest_lat, " and lon ", dest_lon )

    #URL to request the locations for the destination using lat and lon
    url = 'https://api.opentripmap.com/0.1/en/places/radius'

    params = {
        'radius': '5000',  # Set the radius within which to search for locations (in meters)
        'lon': dest_lon,  # Replace with the longitude of your destination
        'lat': dest_lat,  # Replace with the latitude of your destination
        'kinds': 'interesting_places',  # Specify the kind of places to retrieve
        'apikey': api_key,
        'rate': 3,
        'limit': 20
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        if 'error' in data:
            error_message = data['error']['message']
            print(f"Error: {error_message}")
            #return error_message
        else:
            locations = data['features']
            return locations

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    response = requests.get(url, params=params)
    data = response.json()
    print(data)

