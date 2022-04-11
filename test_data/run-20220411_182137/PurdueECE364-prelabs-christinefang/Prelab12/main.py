import flask
import sqlite3
from pprint import pprint as pp
import datetime
import time
import googlemaps
import re

app = flask.Flask(__name__)

API_KEY = 'AIzaSyBhah-q--sGQk-BxKHdzH5SvNtKXA6f-QI'

gmaps = googlemaps.Client(key=API_KEY)


@app.route("/home", methods=['GET','POST'])
def home(): #URL: http://127.0.0.1:5000/home
    if flask.request.method == 'POST':
        origin = flask.request.form['origin']
        destination = flask.request.form['destination']
        if origin == destination:
            return "destination is the same as origin"
        #pp(dir(gmaps))

        with open("directions.tsv",'w') as fp:
            
            now = time.time()
            directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=now)
            dist1 = directions_result[0]['legs'][0]['distance']['text']
            #pp(directions_result)
            fp.write(origin + " to " + destination + '\n')
            fp.write('\n')
            fp.write('Directions and distance\n')
            len_steps = len(directions_result[0]['legs'][0]['steps'])
            html_inst = []
            for i in range(len_steps):
                out = re.sub('<[^>]+>', ' ', directions_result[0]['legs'][0]['steps'][i]['html_instructions'])
                dist = directions_result[0]['legs'][0]['steps'][i]['distance']['text']
                html_inst.append([out,dist])
                fp.write(dist +' '+ out + '\n')
            fp.write('\n')
            resultd = gmaps.geocode(destination)
            if 'lat' in resultd[0]['geometry']['location']:
                lat = resultd[0]['geometry']['location']['lat']
                lng = resultd[0]['geometry']['location']['lng']
                loc = str(lat) +', '+ str(lng)
            else:
                return "Not a real address"
        
            places_result = gmaps.places_nearby(location = loc, radius = 100, type = 'food')
            len_place = len(places_result['results'])

            name = []
            fp.write('Nearby Places with rating\n')
            for i in range(min(len_place,10)):
                if 'rating' in places_result['results'][i]:
                    if places_result['results'][i]['rating'] >= 4:
                        pla = places_result['results'][i]['name']
                        rat = "{:.1f}".format(places_result['results'][i]['rating'])
                        name.append([pla,rat])
                        fp.write(str(rat) + ' ' + pla + '\n')

        return flask.render_template("results.html", origin=origin, destination=destination, dist=dist1, html_inst=html_inst, name=name)
    else:
        return flask.render_template("form.html")

@app.route('/download', methods=['GET', 'POST'])
def download():
    return flask.send_file('directions.tsv', as_attachment=True)


if __name__ == '__main__':
	# Start the server
	app.run(port=5000, host='127.0.0.1', debug=True, use_evalex=False)