import flask
from flask import request
import sqlite3

app = flask.Flask(__name__)


@app.route("/home", methods=['GET', 'POST'])
def home(): #URL: http://127.0.0.1:8001/home
	dictionary  = {"Hello": "World"}
	return dictionary

@app.route("/create_confirm", methods=['POST'])
def create_confirm():
	return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name, UID = UID, pos = pos)


@app.route("/create", methods=['GET','POST'])
def form():
	return flask.render_template("form.html")

@app.route("/form_submit", methods=['POST'])
def submit_form():
	first_name = flask.request.form['fname']
	last_name = flask.request.form['lname']
	UID = flask.request.form['UID']
	pos = flask.request.form['pos']

	conn = sqlite3.connect('data/company.db')
	cursor = conn.cursor()
	# cursor.execute(employees)
	prep = str('''INSERT INTO employees(first_name, last_name, id, position) VALUES ("'''+first_name+'''" ,"'''+last_name+'''" ,'''+UID+''' ,"'''+pos+'''")''')
	cursor.execute(prep)

	print("Data Inserted in the table: ")
	data=cursor.execute('''SELECT * FROM employees''')
	for row in data:
		print(row)
	conn.commit()
	conn.close()
	return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name, UID = UID, pos = pos)

@app.route("/view_all", methods=['GET', 'POST'])
def view_all(): #URL:http://127.0.0.1:8001/view_all
	db_dict = {}
	conn = sqlite3.connect('data/company.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from employees")
	for element in (fetchall.fetchall()):
		db_dict.update({element[2]: [element[0], element[1], element[3]]})
	# print(db_dict)
	return flask.render_template('alltable.html', data = db_dict)

@app.route("/view", methods=['GET','POST']) #
def viewspec(): #URL: http://127.0.0.1:8001/view?emp_id=2
	db_dict = {}
	emp_id = request.args.get('emp_id')
	# print(emp_id)
	# return flask.render_template("form.html")

	conn = sqlite3.connect('data/company.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from employees")
	for element in (fetchall.fetchall()):
		if int(element[2]) == int(emp_id):
			# print("kay")
			db_dict.update({element[2]: [element[0], element[1], element[3]]})
		# print(element[2])

	# print(db_dict)
	return flask.render_template('alltable.html', data = db_dict)

@app.route("/view/<emp_id>", methods=['GET','POST']) #
def viewspecdynamic(emp_id): #URL: http://127.0.0.1:8001/view?emp_id=2
	db_dict = {}
	# emp_id = request.args.get('emp_id')
	# print(emp_id)
	# return flask.render_template("form.html")

	conn = sqlite3.connect('data/company.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from employees")
	for element in (fetchall.fetchall()):
		if int(element[2]) == int(emp_id):
			# print("kay")
			db_dict.update({element[2]: [element[0], element[1], element[3]]})
		# print(element[2])

	# print(db_dict)
	return flask.render_template('alltable.html', data = db_dict)


if __name__ == '__main__':
	# Start the server
	app.run(port=8000, host='127.0.0.1', debug=True, use_evalex=False)