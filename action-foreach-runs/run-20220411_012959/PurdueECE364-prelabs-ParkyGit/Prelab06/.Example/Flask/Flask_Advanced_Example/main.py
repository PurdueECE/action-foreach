import flask
import sqlite3

#https://www.youtube.com/watch?v=D6mgVOF2Ov8

app = flask.Flask(__name__)

@app.route("/grocery/all", methods=['GET', 'POST'])
def grocery_all(): #URL: http://127.0.0.1:8001/grocery/all
	db_dict = {}
	conn = sqlite3.connect('data/grocery.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from grocery")
	for element in (fetchall.fetchall()):
		db_dict.update({element[1]: element[2]})
	return db_dict

@app.route("/grocery/alljinja", methods=['GET', 'POST'])
def grocery_alljinja(): #URL:http://127.0.0.1:8001/grocery/alljinja
	db_dict = {}
	conn = sqlite3.connect('data/grocery.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from grocery")
	for element in (fetchall.fetchall()):
		db_dict.update({element[1]: element[2]})
	print(db_dict)
	return flask.render_template('jinjaexample.html', data = db_dict)


@app.route("/grocery/view", methods=['GET', 'POST'])
def grocery_display(): #URL:http://127.0.0.1:8001/grocery/view?gcode=101
	id = flask.request.args.get('gcode')
	conn = sqlite3.connect('data/grocery.db')
	c = conn.cursor()
	grocery = (c.execute("SELECT name,count from grocery where id = ?", (id,)).fetchall())
	message = f"We need {grocery[0][1]} {grocery[0][0]} "
	return message


@app.route("/grocery/view/<gcode>", methods=['GET', 'POST'])
def grocery_display_dynamic(gcode): #URL:http://127.0.0.1:8001/grocery/view/101
	id = gcode
	conn = sqlite3.connect('data/grocery.db')
	c = conn.cursor()
	grocery = (c.execute("SELECT name,count from grocery where id = ?", (id,)).fetchall())
	message = f"We need {grocery[0][1]} {grocery[0][0]} "
	return message


if __name__ == '__main__':
	# Start the server
	app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)