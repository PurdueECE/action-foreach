import flask

app = flask.Flask(__name__)


@app.route("/home", methods=['GET', 'POST'])
def home(): #URL: http://127.0.0.1:8001/home
	dictionary  = {"Hello": "World"}
	return dictionary


@app.route("/calculate", methods  = ['POST'])
def calulate(): #http://127.0.0.1:8001/calculate (will not work as no GET method defined for this API)
	return "Done"

@app.route("/form", methods=['GET','POST'])
def form():
	return flask.render_template("form.html")

@app.route("/form_submit", methods=['POST'])
def submit_form():
	first_name = flask.request.form['fname']
	last_name = flask.request.form['lname']
	print(first_name)
	print(last_name)
	# return "Thank you for submitting the form"
	return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name)

if __name__ == '__main__':
	# Start the server
	app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)