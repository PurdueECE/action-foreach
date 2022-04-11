import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/form", methods=['GET','POST'])
def form():
	return flask.render_template("form.html")

@app.route("/form_submit", methods=['GET', 'POST'])
def submit_form():

	con = sqlite3.connect('q3_data.db')
	c = con.cursor()
	first_name = flask.request.form['fname']
	last_name = flask.request.form['lname']
	age = flask.request.form['age']
	c.execute("INSERT INTO database (name, lname, age) VALUES(?,?,?)",
			  (first_name, last_name, age))
	con.commit()
	print(first_name)
	print(last_name)
	return "Thank you for submitting the form"
	# return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name)

if __name__ == '__main__':
	# Start the server
	app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)