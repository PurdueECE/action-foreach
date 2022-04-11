from cgitb import html
from logging import raiseExceptions
from operator import methodcaller

import os
import re
from pickle import GET
from re import L
import sqlite3 # List of module import statements
import sys
import googlemaps
import urllib3.request
import time
from pprint import pprint as pp
from turtle import position
import flask 
from torch import equal # Each one on a line

API_KEY = 'AIzaSyDNTIs17Y3_0gDn4bzXlyQGJ3IADjw_g58'
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
        # print(resDict)
        steps = directions_result[0]['legs'][0]['steps']
        for dictionary in steps:
            for key in dictionary:
                if key == 'distance':
                    distance.append(dictionary[key]['text'])
                if key == 'html_instructions':
                    html_instructions.append(dictionary[key])
        # print(directions)
    return flask.render_template('page.html')

@app.route("/results", methods=['GET','POST'])
def results():
    # print(html_instructions)
    html = "http://127.0.0.1:8001/results"
    clean_instr = re.compile('<.*?>')
    new_instr = [re.sub(clean_instr, '\n', x) for x in html_instructions]
    # print(new_instr)
    directions = list(zip(distance, new_instr))
    resDict = dict(zip(name, rating))
    # http = urllib3.PoolManager()
    # r = http.request('GET', html, preload_content=False)

    # with open(path, 'w') as out:
    #     while True:
    #         data = r.read(chunk_size)
    #         if not data:
    #             break
    #         out.write(data)
    # r.release_conn()
    # print(resDict)
    return flask.render_template("results.html", resDict = resDict, directions = directions, distance = distance, instr = html_instructions) 



if __name__ == "__main__":
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)