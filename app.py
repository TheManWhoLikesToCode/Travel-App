from flask import Flask, render_template, redirect, url_for, request
from flask_behind_proxy import FlaskBehindProxy
from tourism import get_locations_to_explore

app = Flask(__name__)
proxied = FlaskBehindProxy(app)


@app.route('/', methods=['GET', 'POST'])
def todo():
    # Add your logic for todo here
    print(request.form)
    if request.method == 'POST':
        location_search = request.form.get('search')
        print("This is location search", location_search)
        location_list = get_locations_to_explore(location_search)
        print("This is location list", location_list)
        return render_template("todo.html", title="ForecastFlyer", subtitle="Results", results=location_list)
    return render_template("todo.html", title="ForecastFlyer - To Do")
    
@app.route('/destinations', methods=['GET', 'POST'])
def destinations():
    # Add your logic for destinations here
    return render_template("destinations.html", title="ForecastFlyer - Destinations")

@app.route('/about_us', methods=['GET'])
def about_us():
    return render_template("about_us.html", title="ForecastFlyer - About Us")

if __name__ == '__main__':
    app.config['SECRET_KEY'] = "This is a secret key"
    app.run(debug=True, host="0.0.0.0", port=5001)
