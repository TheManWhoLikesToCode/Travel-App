# Travel Destination Finder 🗺️

This web application helps travelers find interesting destinations and attractions around the places they want to visit.

## Overview

The app allows users to enter a destination city or country. It will then call external APIs to find popular landmarks, activities, and points of interest within a radius of the destination. These are displayed on a results page to give travel inspiration.

The frontend uses Flask to render HTML templates powered by Jinja. Styling is done with vanilla CSS.

The backend makes calls to the OpenTripMap APIs to get geographic coordinates of the destination and nearby points of interest. Python requests module is used to interact with the APIs. 

## Features

- Search for a destination city or country ✈️
- Returns list of attractions, activities, and places to see 🏰
- Clean and responsive design 💻
- Integrates geographic/travel data from OpenTripMap 🌎

## Running Locally

To run the app locally:

1. Clone the repo 👯
2. Create a virtual environment 
3. Install requirements with `pip install -r requirements.txt` ⚙️ 
4. Run `python app.py` ▶️
5. Access the app at http://localhost:5001 🚀

## Technologies

- **Frontend:** HTML, Jinja, Flask, CSS
- **Backend:** Python
- **External APIs:** OpenTripMap, aviationstack

## Potential Improvements

Some ideas for future iterations:

- Allow sorting results by rating, distance, etc 🏅
- Integrate maps to show attraction locations 🗺️
- Save past searches and destinations ✔️

Let me know if you need any clarification or have additional ideas for the README! 📝