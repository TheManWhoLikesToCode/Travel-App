import random
from flask import Flask, render_template, redirect, url_for, request
from flask_behind_proxy import FlaskBehindProxy
from tourism import get_locations_to_explore
from weather import getForecast
from flask_sqlalchemy import SQLAlchemy
from aviation import get_flight
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db/travel.db')
db = SQLAlchemy(app)


class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True,
                   default=lambda: random.randint(1000000, 9999999))
    Departure_Location = db.Column(db.String(80), nullable=False)
    Arrival_Location = db.Column(db.String(80), nullable=False)
    Departure_Date = db.Column(db.String(80), nullable=False)
    Arrival_Date = db.Column(db.String(80), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.form)
    if request.method == 'POST':
        flight_dep = request.form.get('from')
        flight_to = request.form.get('to')
        print("This is departing airport", flight_dep)
        print("This is arriving airport", flight_to)
        flight_list = get_flight(flight_dep, flight_to)
        subtitle = f"Results {flight_dep} to {flight_to}" if flight_list else "No Results Found"
        print("This is flight list", flight_list)
        return render_template("home.html", title="ForecastFlyer", subtitle=subtitle, results=flight_list)
    return render_template("home.html", title="ForecastFlyer")


@app.route('/destinations', methods=['GET', 'POST'])
def destinations():
    flight_list = None
    if request.method == 'POST':
        Departure_Location = request.form.get('from')
        Arrival_Location = request.form.get('to')
        Departure_Date = request.form.get('departureDate')
        Arrival_Date = request.form.get('returnDate')

        # Validate form data
        if not Departure_Location or not Arrival_Location or not Departure_Date or not Arrival_Date:
            print("Invalid form data")
            return redirect(url_for('destinations'))

        new_destination = Destination(
            Departure_Location=Departure_Location,
            Arrival_Location=Arrival_Location,
            Departure_Date=Departure_Date,
            Arrival_Date=Arrival_Date
        )
        db.session.add(new_destination)
        db.session.commit()
        print(f"New destination added: {new_destination.id}")

        # Call the get_flight function
        flight_list = get_flight(Departure_Location, Arrival_Location)
        print("This is flight list", flight_list)

    destinations = Destination.query.all()
    print(f"Retrieved {len(destinations)} destinations from the database:")
    for destination in destinations:
        print(f"ID: {destination.id}, Departure: {destination.Departure_Location}, Arrival: {destination.Arrival_Location}, Departure Date: {destination.Departure_Date}, Arrival Date: {destination.Arrival_Date}")

    return render_template("destinations.html", title="ForecastFlyer - Destinations", destinations=destinations, flights=flight_list)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        destination = request.form.get('destination')
        if destination:
            finaldays = getForecast(destination[0])
            finalforecast = getForecast(destination[1])
            return render_template("weather.html", len=len(finaldays), finaldays=finaldays, finalforecast=finalforecast)
    return render_template("weather.html", title="ForecastFlyer - Weather")

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        destination = request.form.get('destination')
        if destination:
            results = get_locations_to_explore(destination)
            subtitle = "Results" if results else "No Results Found"
            return render_template("todo.html", title="ForecastFlyer", subtitle=subtitle, results=results)
    return render_template("todo.html", title="ForecastFlyer - To Do")


@app.route('/about_us', methods=['GET'])
def about_us():
    return render_template("about_us.html", title="ForecastFlyer - About Us")


if __name__ == '__main__':
    app.config['SECRET_KEY'] = "This is a secret key"
    app.run(debug=True, host="0.0.0.0", port=5001)
