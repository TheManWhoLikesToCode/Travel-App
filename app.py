from flask import Flask, render_template, redirect, url_for, request
from flask_behind_proxy import FlaskBehindProxy
from tourism import get_locations_to_explore
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/travel.db'
db = SQLAlchemy(app)


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Departure_Location = db.Column(db.String(80), nullable=False)
    Arrival_Location = db.Column(db.String(80), nullable=False)
    Departure_Date = db.Column(db.String(80), nullable=False)
    Arrival_Date = db.Column(db.String(80), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.form)
    if request.method == 'POST':
        location_search = request.form.get('search')
        print("This is location search", location_search)
        location_list = get_locations_to_explore(location_search)
        print("This is location list", location_list)
        return render_template("home.html", title="ForecastFlyer", subtitle="Results", results=location_list)
    return render_template("home.html", title="ForecastFlyer")


@app.route('/destinations', methods=['GET', 'POST'])
def destinations():
    if request.method == 'POST':
        Departure_Location = request.form.get('Departure_Location')
        Arrival_Location = request.form.get('Arrival_Location')
        Departure_Date = request.form.get('Departure_Date')
        Arrival_Date = request.form.get('Arrival_Date')
        new_destination = Destination(
            Departure_Location=Departure_Location,
            Arrival_Location=Arrival_Location,
            Departure_Date=Departure_Date,
            Arrival_Date=Arrival_Date
        )
        db.session.add(new_destination)
        db.session.commit()
        return redirect(url_for('destinations'))
    destinations = Destination.query.all()
    return render_template("destinations.html", title="ForecastFlyer - Destinations", destinations=destinations)


@app.route('/todo', methods=['GET', 'POST'])
def todo():
   # Add your logic for todo here
    return render_template("todo.html", title="ForecastFlyer - To Do")


@app.route('/about_us', methods=['GET'])
def about_us():
    return render_template("about_us.html", title="ForecastFlyer - About Us")


if __name__ == '__main__':
    app.config['SECRET_KEY'] = "This is a secret key"
    app.run(debug=True, host="0.0.0.0", port=5001)



