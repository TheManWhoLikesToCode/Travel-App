import requests


def get_flight(dep, arr, dep_date=None, arr_date=None):
    # Check if departure and arrival locations are provided
    if not dep or not arr:
        print("Departure and arrival locations must be provided.")
        return None

    api_key = 'fa66b9dfe7b7942d3d8ae8944c836c6a'
    url = 'http://api.aviationstack.com/v1/flights'

    # Set the required parameters
    params = {
        'access_key': api_key,
        'dep_iata': dep,
        'arr_iata': arr,
        'limit': 10
    }

    # Add dates to parameters if they are provided
    if dep_date:
        params['dep_date'] = dep_date
    if arr_date:
        params['arr_date'] = arr_date

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if 'error' in data:
            error_message = data['error']['message']
            print(f"Error: {error_message}")
            return None
        else:
            flights = data['data']
            return flights

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
