from cgitb import html
from logging import raiseExceptions
from operator import methodcaller
import re
import os
from threading import local
import googlemaps
import time
from pprint import pprint as pp
from turtle import position
import flask 
import jpype
import wget
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from torch import equal # Each one on a line

API_KEY = 'AIzaSyC9RSQw6ksQE6B6bii-enerdoaZI0pWx-8'
gmaps = googlemaps.Client(key=API_KEY)
app = flask.Flask(__name__)
html_instructions = []
distance = []
rating = []
name = []
directions = []
resDict = {}

@app.route("/home", methods=['GET','POST'])
def home(): #URL: http://127.0.0.1:8001/home
    if flask.request.method == 'POST':
        origin = flask.request.form['origin']
        dest = flask.request.form['destination']
        if origin == dest:
            return "Your origin is the same as your destination."
        now = time.time()
        directions_result = gmaps.directions(origin, dest, mode="driving", departure_time=now)
        geocode = gmaps.geocode(dest)
        lat = geocode[0]["geometry"]["location"]['lat']
        lng = geocode[0]["geometry"]["location"]['lng']
        places_result = gmaps.places_nearby(location = f"{lat}, {lng}", radius = 100, open_now = False, type = 'restaurant')
        restaurants = places_result['results']
        if len(restaurants) > 10:
            restaurants = restaurants[:10]
        for restaurant in restaurants:
            for key in restaurant:
                if key == "name":
                    name.append(restaurant[key])
                if key == "rating" and restaurant[key] >= 4:
                    rating.append(restaurant[key])
        resDict = dict(zip(name, rating))

        print(resDict)

        steps = directions_result[0]['legs'][0]['steps']
        # print(steps)
        for dictionary in steps:
            for key in dictionary:
                if key == 'distance':
                    distance.append(dictionary[key]['text'])
                if key == 'html_instructions':
                    html_instructions.append(dictionary[key])
        print(directions)
    return flask.render_template('form.html')

@app.route("/results", methods=['GET','POST'])
def results():
    # print(html_instructions)
    # html = "http://127.0.0.1:8001/results"
    # local = "results.html"
    clean_instr = re.compile('<.*?>')
    new_instr = [re.sub(clean_instr, '\n', x) for x in html_instructions]
    directions = list(zip(distance, new_instr))
    resDict = dict(zip(name, rating))
    return flask.render_template("final.html", resDict = resDict, directions = directions) 
@app.route("/download", methods=['GET','POST'])
def download():
    url = "http://127.0.0.1:8006/results"
    html = "templates/dir&res.html"
    if os.path.exists(html):
        os.remove(html)
    wget.download(url, html)
    workbook = Workbook(html)
    if os.path.exists("results.tsv"):
        os.remove("results.tsv")
    workbook.save("results.tsv")
    return "File donwloaded successfully!"
if __name__ == "__main__":
    app.run(port=8006, host='127.0.0.1', debug=True, use_evalex=False)