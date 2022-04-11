####################################
#   Author:     Denny Nowak
#   Email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       02/19/2022
####################################

import os
import sys
import flask
import sqlite3

app = flask.Flask(__name__)
app.secret_key = 'sdfkajfajsdkafdskl;jf;sdjlfsdjk;l234231423' # used for sessions

# Problem 1
@app.route("/create", methods=['GET','POST'])
def form():
	return flask.render_template("create.html")

@app.route("/form_submit", methods=['POST'])
def submit_form():
    # Get values
    firstName = flask.request.form['fname']
    lastName = flask.request.form['lname']
    idVar = flask.request.form['id']
    position = flask.request.form['position']

    # Insert into table
    connection = sqlite3.connect('data/company.db')
    c = connection.cursor()
    c.execute("INSERT INTO employees (first_name, last_name, id, position) VALUES (?, ?, ?, ?)", (firstName, lastName, idVar, position))
    connection.commit()

    return flask.render_template("create.html")

# Problem 2
@app.route("/view", methods=['GET', 'POST'])
def employeeDisplay():
    # Get ID from database
    idVar = flask.request.args.get('emp_id')
    connection = sqlite3.connect('data/company.db')
    c = connection.cursor()
    employees = (c.execute("SELECT first_name, last_name, position from employees where id = ?", (idVar,)).fetchall())
    flask.session["ID"] = idVar 

    return flask.render_template('view.html', first_name = employees[0][0], last_name = employees[0][1], position = employees[0][2], id = idVar)

@app.route("/delete_employee", methods=['POST'])
def deleteEmployee():
    # Get employee id for deletion
    idVar = flask.session.get("ID")
  
    # Delete employee from database
    connection = sqlite3.connect('data/company.db')
    c = connection.cursor()
    employees = (c.execute("DELETE from employees where id = ?", (idVar,)).fetchall())
    connection.commit()

    return f"Employee Deleted"

@app.route("/view/<emp_id>", methods=['GET', 'POST'])
def deleteEmployeeDynamic(emp_id):
    # Get dynamic ID from database
    idVar = emp_id
    connection = sqlite3.connect('data/company.db')
    c = connection.cursor()
    employees = (c.execute("SELECT first_name, last_name, position from employees where id = ?", (idVar,)).fetchall())
    flask.session["ID"] = idVar 

    return flask.render_template('view.html', first_name = employees[0][0], last_name = employees[0][1], position = employees[0][2], id = idVar)

# Problem 3
@app.route("/view_all", methods=['GET','POST'])
def viewAll():
    # Get database values and return Jinja template
    dbDict = {}
    connection = sqlite3.connect('data/company.db')
    c = connection.cursor()
    fetchall = c.execute("SELECT * from employees")
    for element in (fetchall.fetchall()):
        dbDict.update({element[2]: [element[0], element[1], element[3]]})

    return flask.render_template('viewAll.html', data = dbDict)

if __name__ == '__main__':
    # Start server
    app.run(port=5503, host='127.0.0.1', debug=True, use_evalex=False)