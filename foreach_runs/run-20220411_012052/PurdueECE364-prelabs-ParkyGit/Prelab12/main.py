from pprint import pprint as pp
import time
import os
from PIL import Image
import googlemaps
import flask
from flask import send_file
from flask import request
import pandas as pd
import csv
from bs4 import BeautifulSoup
key = "AIzaSyDABxvwgZuOIRd-JXNCDQXXgB7mHk0J3lA"
app = flask.Flask(__name__)

		
@app.route("/download", methods=['POST'])
def download():
	return send_file('output.tsv', as_attachment=True)
	# return flask.render_template("result.html")


@app.route("/create_confirm", methods=['POST'])
def create_confirm():
	return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name)


@app.route("/create", methods=['GET','POST'])
def form():
	return flask.render_template("form.html")


@app.route("/form_submit", methods=['POST'])
def submit_form():
	first_name = flask.request.form['fname']
	last_name = flask.request.form['lname']
	gmaps = googlemaps.Client(key=key)

	a = first_name
	b = last_name

	now = time.time()
	directions_result = gmaps.directions(a,	b, mode="walking", departure_time=now)

	directions_steps = directions_result[0]["legs"][0]["steps"]
	x = 0
	dists = []
	htmlinst = []
	for item in directions_steps:
		dists.append(directions_steps[x]["distance"])
		htmlinst.append(directions_steps[x]["html_instructions"])
		x = x + 1

	endLocation = directions_result[0]["legs"][0]["end_location"]
	# pp(endLocation)
	endLocationStr = str(endLocation["lat"]) + ", " + str(endLocation["lng"])
	places = []
	ratings = []
	places_result = gmaps.places_nearby(location = endLocationStr, radius = 100, open_now = False, type = 'point_of_interest')
	# pp(places_result["results"])
	x = 0
	results = places_result["results"]
	for item in results:
		food = 0
		placeType = results[x]["types"]
		for item in placeType:
			if item == "food":
				food = 1
		if len(places) >= 10:
			break
		rate = 0
		# pp(results[x])
		# pp(results[x]["name"])
		try:
			# pp(results[x]["rating"])
			rate = results[x]["rating"]
		except KeyError:  # Throws Errors but does not crash the program
			rate = 0
		if rate >= 4 and food == 1:
			places.append(results[x]["name"])
			ratings.append(rate)
		x = x+1
	print(places)
	print(ratings)

	#generate HTML
	html = """<HTML>
	<body>
		<h1>Directions</h1>
		<table>
			{0}
		</table>
	</body>
	<body>
		<form action="/download" method="POST" id = "form">
		<input type="submit" value="Download TSV">
		</form>
   	</body>
	</HTML>"""

	items = []
	for x in range(len(dists)):
		entry = []
		# print(htmlinst[x], dists[x]["text"])
		entry.append(htmlinst[x])
		entry.append(dists[x]["text"])
		items.append(entry)
	placesRatings = []
	for x in range(len(places)):
		entry = []
		entry.append(places[x])
		entry.append(str(ratings[x]))
		placesRatings.append(entry)
	# print(placesRatings)
	# items = [['Leeds', '40alksdjfweijoewfijweofijweoifjodijosijdvoijisdodfiso'], ['Bristol', '32'], ['Manchester', '41']]
	tr = "<tr>{0}</tr>"
	td = "<td>{0}</td>"
	subitems = [tr.format(''.join([td.format(a) for a in item])) for item in items]
	# print html.format("".join(subitems)) # or write, whichever
	# print(subitems)

	subitems.append('<tr><td> </td><td> </b></td></tr>')
	subitems.append('<tr><td> </td><td> </b></td></tr>')
	midheader = '<tr><td><b>Nearby Places</b></td><td><b>Ratings</b></b></td></tr>'
	subitems.append('<tr><td> </td><td> </b></td></tr>')
	subitems.append(midheader)

	tr = "<tr>{0}</tr>"
	td = "<td>{0}</td>"
	subitems2 = [tr.format(''.join([td.format(a) for a in item])) for item in placesRatings]

	subitems2str = ""
	for x in subitems2:
		subitems2str = subitems2str + x

	file_ = open('templates/result.html', 'w')
	file_.write(html.format(("".join(subitems)) + subitems2str))
	file_.close()

	path = 'templates/result.html'
	data = []
	

	#Convert to CSV, then TSV
	list_header = []
	soup = BeautifulSoup(open(path),'html.parser')
	header = soup.find_all("table")[0].find("tr")
	
	for items in header:
		try:
			list_header.append(items.get_text())
		except:
			print("No items in header")

	HTML_data = soup.find_all("table")[0].find_all("tr")[1:]	
	for element in HTML_data:
		sub_data = []
		for sub_element in element:
			try:
				sub_data.append(sub_element.get_text())
			except:
				continue
		data.append(sub_data)

	dataFrame = pd.DataFrame(data = data, columns = list_header)
	dataFrame.to_csv('input.csv')
	csv.writer(open('output.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open("input.csv")))
	if os.path.exists("input.csv"):
		os.remove("input.csv")

	return flask.render_template('result.html')


if __name__ == '__main__':
	# Start the server
	app.run(port=8000, host='127.0.0.1', debug=True, use_evalex=False)