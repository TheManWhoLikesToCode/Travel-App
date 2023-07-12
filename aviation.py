import requests

api_key = '0592d0699fcfdbc310e9a112b7deb3b9'
url = 'http://api.aviationstack.com/v1/flights'

# Get user input for departure and arrival airports
#departure_airport = input("Enter the departure airport: ")
#arrival_airport = input("Enter the arrival airport: ")

departure_airport = "KLAX"
arrival_airport = "KIAD"

# Set the required parameters
params = {
    'access_key': api_key,
    'dep_icao': departure_airport,
    'arr_icao': arrival_airport,
    'limit': 5
}

# Make the API request
response = requests.get(url, params=params)

# Get the JSON response
data = response.json()

# Access the flight data
flights = data['data']
print(flights)

#for flight in flights:
#    print("This is the departure" , flight['departure']['airport'], " and this is the arrival", flight['arrival']['airport'] )
