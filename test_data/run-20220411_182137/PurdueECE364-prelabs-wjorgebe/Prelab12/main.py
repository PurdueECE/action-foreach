from collections import defaultdict
from importlib.resources import path
from pprint import pprint as pp
from sys import stderr
import flask
import googlemaps
import time
import csv
import re
import sys

API_KEY = 'AIzaSyDaKt1BbzQ3a4VqgNO-PSHAIm5TJGJI59s'
gmaps = googlemaps.Client(key=API_KEY)

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def form():
    return flask.render_template("default.html")

@app.route("/results", methods=['POST'])
def submit_form():
    origin = flask.request.form['origin']
    dest = flask.request.form['destination']

    if origin == dest:
        print("Origin and destination cannot be the same.")
        return flask.redirect("/")

    directions_result = gmaps.directions(origin, dest, mode='driving', departure_time=time.time())
    steps = directions_result[0]['legs'][0]['steps']
    directions = {}
    for idx, dict in enumerate(steps):
        directions[idx] = [dict['distance']['text'], dict['html_instructions']]
    dest_coordinates = (directions_result[0]['legs'][0]['end_location']['lat'], directions_result[0]['legs'][0]['end_location']['lng'])
    nearby_results = gmaps.places_nearby(location=str(dest_coordinates[0]) + "," + str(dest_coordinates[1]), radius=100, type='food')
    nearby_food = {}
    j = 0
    for i in nearby_results['results']:
        if len(nearby_food) >= 10:
            break
        if 'rating' in i.keys() and i['rating'] >= 4.0:
            nearby_food[j] = (i['name'], i['rating'])
            j += 1

    with open('directions.tsv', 'wt') as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(['Directions'])
        tsv_writer.writerow([])
        cleaner = re.compile('<.*?>')
        for key, value in directions.items():
            tsv_writer.writerow([re.sub(cleaner, '', value[1]), value[0]])
        tsv_writer.writerow([])
        tsv_writer.writerow(['Nearby food options'])
        tsv_writer.writerow([])
        for key,value in nearby_food.items():
            tsv_writer.writerow([value[0], value[1]])

    return flask.render_template("results.html", directions = directions, nearby = nearby_food)

@app.route("/download", methods=['GET'])
def download_file():
    return flask.send_file("directions.tsv", as_attachment=True)
    

if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)