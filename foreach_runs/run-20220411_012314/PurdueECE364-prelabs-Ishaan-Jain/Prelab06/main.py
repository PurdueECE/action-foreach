from turtle import position
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if flask.request.method == 'POST':
        first_name= flask.request.form['fname']
        last_name = flask.request.form['lname']
        position = flask.request.form['pos']
        id = flask.request.form['ID']
        with sqlite3.connect("data/company.db") as data:
            cur = data.cursor()
            cur.execute("INSERT INTO employees (first_name,last_name,id,position) VALUES (?,?,?,?)", (first_name,last_name,id,position))
            data.commit()   
    return flask.render_template('form.html')     


@app.route("/view/emp_id/<xyz>", methods=['GET', 'POST'])
def extract(xyz):
    i_d = xyz
    if flask.request.method == 'GET':
        conn = sqlite3.connect('data/company.db')
        c = conn.cursor()
        match = (c.execute("SELECT first_name,last_name,position from employees where id = ?", (i_d,)).fetchall())

    return   flask.render_template('form2.html',id = i_d,first_name = match[0][0], last_name= match[0][1],position=match[0][2])

@app.route("/delete", methods=['POST'])
def delete():
    if flask.request.method == 'POST':
        con = sqlite3.connect("data/company.db")
        cursor = con.cursor()
        id = flask.request.form['id']
        cursor.execute('DELETE FROM employees WHERE id = ?',(id,))
        con.commit()
        con.close()
        return "Deletion Succesfull"

@app.route("/view_all", methods=['GET', 'POST'])
def view_all(): #URL:http://127.0.0.1:8001/grocery/alljinja
	lis = []
	conn = sqlite3.connect('data/company.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from employees")
	for element in (fetchall.fetchall()):
		lis.append(element)
	print(lis)
	return flask.render_template('jinja.html', data = lis)



if __name__ == '__main__':
	# Start the server
	app.run(port=8002, host='127.0.0.1', debug=True, use_evalex=False)