#####################################
# Author: Aedan Frazier
# Email : frazie35@purdue.edu
# ID    : ee364a06
# Date  : 4/6/2022
#####################################

from pprint import pprint as pp
import datetime
import time
import googlemaps
import flask
import sqlite3

API_KEY = 'AIzaSyDLyPqDxA3e9YmgcX50dN9-ND4dYOAaAcw'

gmaps = googlemaps.Client(key=API_KEY)

pp(dir(gmaps))

now = time.time()
directions_result = gmaps.directions("Purdue Airport",
                                     "Ross Ade Stadium",
                                     mode="walking",
                                     departure_time=now)
pp(directions_result)




app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('form.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True, use_evalex=False)
