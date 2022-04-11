################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu 
#   ID:     ee364b14
#   Date:   04/07/2022
################################
import flask
import time
import googlemaps
import csv
API_KEY = 'AIzaSyA1czOvDNlSuIue67qeD92DRj0Km_4tClw'
gmaps = googlemaps.Client(key=API_KEY)
app = flask.Flask(__name__)
app.secret_key = 'asdfa12312fsdasfd' # used for sessions


# Inputs for origin and destination
@app.route("/input", methods=['GET', 'POST'])
def form():
    return flask.render_template("input.html")


# Find directions and nearby food options submission
@app.route("/results", methods=['POST'])
def submit_form():
    # Get values
    origin = flask.request.form['origin']
    destination = flask.request.form['destination']
    
    # Check for same address
    if origin == destination:
        return flask.render_template("input.html")

    # Find directions and get html_instructions and distance for each leg
    instr = []
    distance = []
    dirDict = {}
    now = time.time()

    # Try direction result
    try:
        directionsResult = gmaps.directions(origin, destination, mode="walking", departure_time=now)
    except:
        return flask.render_template("input.html")
    
    # Check for no results
    if not directionsResult:
        return flask.render_template("input.html")
    
    for leg in directionsResult[0]['legs']:
        for step in leg['steps']:
            dirDict.update({step['html_instructions'] : step['distance']})

    # Find Long and Lat values of destination
    geoResult = gmaps.geocode(destination)

    # Check for no results
    if not geoResult:
        return flask.render_template("input.html")
    
    locationVals = geoResult[0]['geometry']['location']
    locationStr = str(locationVals['lat']) + ', ' + str(locationVals['lng'])

    # Find nearby food places
    placesResult = gmaps.places_nearby(location = locationStr, radius = 100) 

    # Check for no results
    if not placesResult:
        return flask.render_template("input.html")

    placeDict = {}
    for place in placesResult['results']:
        # Filter for food
        if 'types' in place:
            if 'food' in place['types']:
                # Filter for rating
                if 'rating' in place:
                    if place['rating'] >= 4:
                        # Filter out first 10 results
                        placeDict.update({place['name'] : place['rating']})
                        if len(placeDict) == 10:
                            break
    
    # Save values
    flask.session['place'] = placeDict
    flask.session['dir'] = dirDict
    return flask.render_template("result.html", places = placeDict, dir = dirDict)


# Create and send TSV file
@app.route("/download", methods=['POST'])
def download_tsv():
    # Get values
    placeDict = flask.session.get('place')
    dirDict = flask.session.get('dir')

    # Write to file
    with open('prelab12.tsv', 'w') as fptr:
        tsv = csv.writer(fptr, delimiter='\t')
        tsv.writerow(['instruction', 'distance'])
        for key, value in dirDict.items():
            tsv.writerow([key, value['text']])
        tsv.writerow(['name', 'rating'])
        for key, value in placeDict.items():
            tsv.writerow([key, value])

    # Send file
    return flask.send_file('./prelab12.tsv', as_attachment=True)
    


if __name__ == '__main__':
    # Start server
    app.run(port=5503, host='127.0.0.1', debug=True, use_evalex=False)
