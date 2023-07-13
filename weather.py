from flask import Flask, render_template
from pyowm.owm import OWM
import pyowm

API_key = '544e03ea5ba29e43a20170a9a886f978'
owm = OWM(API_key)
place = 'Atlanta'
weather_mgr = owm.weather_manager()
observation = weather_mgr.weather_at_place(place)

weatherlist = []
three_h_forecast = weather_mgr.forecast_at_place(place, '3h').forecast
nr_of_weathers = len(three_h_forecast)


day0 = []
day1 = []
day2 = []
day3 = []
day4 = []
day5 = []

dayslist = []
weatherlist = []
for weather in three_h_forecast:
    dayslist.append(weather.reference_time('iso')[5:10])
    weatherlist.append(weather.detailed_status)


day0 = []
day1 = []
day2 = []
day3 = []
day4 = []
day5 = []

dayslist = []
weatherlist = []
for weather in three_h_forecast:
    dayslist.append(weather.reference_time('iso')[5:10])
    weatherlist.append(weather.detailed_status)

days = []
for day in dayslist:
    if day not in days:
        days.append(day)

for i in range(len(weatherlist)):
    if len(days) == 6:
        if i == 0:
            day0.append(weatherlist[0])
        if i in range(1, 9):
            day1.append(weatherlist[i])
        if i in range(9,17):
            day2.append(weatherlist[i])
        if i in range(17, 25):
            day3.append(weatherlist[i])
        if i in range(25, 33):
            day4.append(weatherlist[i])
        if i in range(33, len(weatherlist)):
            day5.append(weatherlist[i])
    else:
        if i in range(0, 8):
            day1.append(weatherlist[i])
        if i in range(8,16):
            day2.append(weatherlist[i])
        if i in range(16, 24):
            day3.append(weatherlist[i])
        if i in range(24, 32):
            day4.append(weatherlist[i])
        if i in range(32, len(weatherlist)):
            day5.append(weatherlist[i])

if len(days) == 6:
    day0 = max(set(day0), key=day0.count)
    day1 = max(set(day1), key=day1.count)
    day2 = max(set(day2), key=day2.count)
    day3 = max(set(day3), key=day3.count)
    day4 = max(set(day4), key=day4.count)
    day5 = max(set(day5), key=day5.count)
else:
    day1 = max(set(day1), key=day1.count)
    day2 = max(set(day2), key=day2.count)
    day3 = max(set(day3), key=day3.count)
    day4 = max(set(day4), key=day4.count)
    day5 = max(set(day5), key=day5.count)

days =  []
daycast = []

for day in dayslist:
    if day not in days:
        days.append(day)

# print(days)
if len(days) == 6:
    daycast.append((days[0], day0))
    daycast.append((days[1], day1))
    daycast.append((days[2], day2))
    daycast.append((days[3], day3))
    daycast.append((days[4], day4))
    daycast.append((days[5], day5))
else:
    daycast.append((days[0], day1))
    daycast.append((days[1], day2))
    daycast.append((days[2], day3))
    daycast.append((days[3], day4))
    daycast.append((days[4], day5))

# print(daycast)

finaldays = []
finalforecast = []
for i in range(len(daycast)):
    testlist = list(daycast[i])
    for item in testlist:
        finalforecast.append(testlist.pop())
        finaldays.append(testlist.pop())

finaldays = []
finalforecast = []
for i in range(len(daycast)):
    testlist = list(daycast[i])
    for item in testlist:
        finalforecast.append(testlist.pop())
        finaldays.append(testlist.pop())

app = Flask(__name__)


@app.route('/')
def forecast():  # put application's code here
    return render_template("weather.html", len = len(finaldays), finaldays = finaldays, finalforecast = finalforecast)




if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)