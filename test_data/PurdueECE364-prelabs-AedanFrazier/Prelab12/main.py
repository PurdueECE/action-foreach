#####################################
# Author: Aedan Frazier
# Email : frazie35@purdue.edu
# ID    : ee364a06
# Date  : 4/6/2022
#####################################

import keyword
from pprint import pprint as pp
import datetime
import time
import googlemaps
import flask
import sqlite3
import re

API_KEY = 'AIzaSyDLyPqDxA3e9YmgcX50dN9-ND4dYOAaAcw'

gmaps = googlemaps.Client(key=API_KEY)

app = flask.Flask(__name__)


d = []
p = []

@app.route("/")
def index():
    return flask.render_template('form.html')

@app.route("/results",  methods=["POST"])
def directions():
    origin = flask.request.form['origin']
    destination = flask.request.form['destination']
    print("{} -> {}".format(origin, destination))

    now = time.time()
    directions = gmaps.directions(origin, destination, mode="walking", departure_time=now)
    la = directions[0]["legs"][0]["end_location"]["lat"]
    lo = directions[0]["legs"][0]["end_location"]["lng"]
    dirs = dict()
    i = 0
    for node in directions[0]["legs"][0]["steps"]:
        instr = node['html_instructions']
        instr = instr.replace('<b>', '', 100)
        instr = instr.replace('</b>', '', 100)

        instr = re.sub('<.+\>', '', instr)

        dirs[i] = ((instr,node['distance']['text']))
       
        i = i + 1
    places = gmaps.places_nearby(location = "{},{}".format(la,lo), radius = 100, open_now = False, type=["food", "restaurant"])
    food_places = dict()

    try:
        for i in range(0,10):
            name = places["results"][i+1]["name"]
            rating = None
            try:
                rating = places["results"][i+1]["rating"]
            except:
                pass
            food_places[name] = rating
    except:
        pass
        #print("Name: {}, Rating: {}".format(name,rating ))
    #print(food_places)
    global p
    global d
    p = food_places
    d = dirs

    return flask.render_template('directions.html', dirs=dirs, places=food_places)

@app.route("/download",  methods=["POST"])
def download():

    FILE = open("instructions.tsv", "w")

    FILE.write("instruction\tdistance\n")
    for ins in d:
        FILE.write("{}\t{}\n".format(d[ins][0], d[ins][1]))

    FILE.write("\n")
    FILE.write("name\trating\n")
    for key in p:
        FILE.write("{}\t{}\n".format(key, p[key]))

    FILE.close()

    return flask.render_template('download.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True, use_evalex=False)
