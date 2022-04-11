# Copy format

import flask
from flask import request
import sqlite3
app = flask.Flask(__name__)

@app.route("/create", methods=['GET','POST'])
def create(): 
    if flask.request.method == 'POST':
        first_name = flask.request.form['fname']
        last_name = flask.request.form['lname']
        id = flask.request.form['number']
        position = flask.request.form['position']
        with sqlite3.connect('data/company.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO employees (first_name, last_name, id, position) VALUES (?,?,?,?)", 
            (first_name, last_name, id, position))
            connection.commit()
    return flask.render_template('form.html')


@app.route("/view/<xyz>", methods=["GET", "POST"])
def info(xyz):
    id = xyz
    if flask.request.method == 'GET': 
        connection = sqlite3.connect("data/company.db")
        cursor = connection.cursor()
        match = (cursor.execute("SELECT first_name, last_name, position from employees WHERE id = ?", (id,)).fetchall())  
        message = " ".join([str(i) for i in match])
        connection.commit()
        cursor.close()
        connection.close()
        return flask.render_template('info.html', id = id, first_name=match[0][0], last_name=match[0][1], position=match[0][2])
        
@app.route("/delete", methods=['POST'])
def delete():
    if flask.request.method == 'POST':
        connection = sqlite3.connect("data/company.db")
        cursor = connection.cursor()
        id = flask.request.form['id']
        cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
        connection.commit()
        connection.close()
        return "Deleted"


@app.route("/view_all", methods=["GET", "POST"])
def view_all():
    db_dict = []
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    fetchall = c.execute("SELECT * from employees")
    for element in (fetchall.fetchall()):
	    db_dict.append(element)
    return flask.render_template('jinja.html', data = db_dict)
    
if __name__ == "__main__":
    app.run(port=8003, host='127.0.0.1', debug=True, use_evalex=False)

     
