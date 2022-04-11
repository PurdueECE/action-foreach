#################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   03/12/2022
#################################
import flask
import sqlite3
app = flask.Flask(__name__)


@app.route("/create", methods=['GET', 'POST'])
def form():
    return flask.render_template("create.html")


# Example 1
# Insert username and password into dataEx1.db
@app.route("/form_submit", methods=['POST'])
def submit_form():
    # Get values
    user = flask.request.form['user']
    password = flask.request.form['password']
    # Insert into table for Example 1
    # The exploit command updates the password for a given username
    connection = sqlite3.connect('dataEx1.db')
    c = connection.cursor()
    c.executescript("INSERT INTO users (username, password) VALUES ('{0}', '{1}')".format(user, password))
    connection.commit()
    return flask.render_template("create.html")


# Example 2
# Prints username and password from dataEx2.db to terminal given username
@app.route("/form_submit2", methods=['POST'])
def submit_form2():
    # Get values
    user = flask.request.form['user']
    # Get user and password for Example 2
    # The exploit command retrieves all of the user and passwords from the dataEx2.db file
    connection = sqlite3.connect('dataEx2.db')
    c = connection.cursor()
    sqlStr = 'SELECT * FROM users where username = "' + user + '"'
    fetchall = c.execute(sqlStr)
    testDict = {}
    for element in (fetchall.fetchall()):
        testDict.update({element[0]: element[1]})
    print(testDict)
    return flask.render_template("create.html")


# Example 3
# Insert username and password into dataEx5.db
@app.route("/form_submit3", methods=['POST'])
def submit_form3():
    # Get values
    user = flask.request.form['user']
    password = flask.request.form['password']
    # Insert into table for Example 5
    # The exploit command adds an additional row for dataEx5.db users table
    connection = sqlite3.connect('dataEx5.db')
    c = connection.cursor()
    c.executescript("INSERT INTO users (username, password) VALUES ('{0}', '{1}')".format(user, password))
    connection.commit()
    return flask.render_template("create.html")


# Example 4
# Print all usernames and passwords from dataEx4.db to terminal given one username from table
@app.route("/form_submit4", methods=['POST'])
def submit_form4():
    # Get values
    user = flask.request.form['user']
    # Get all user and passwords for Example 4
    # The exploit command retrieves all data from another table (students) and also prints to terminal
    connection = sqlite3.connect('dataEx4.db')
    c = connection.cursor()
    sqlStr = 'SELECT * FROM users ' + user
    fetchall = c.execute(sqlStr)
    testDict = {}
    for element in (fetchall.fetchall()):
        testDict.update({element[0]: element[1]})
    print(testDict)
    return flask.render_template("create.html")


# Example 5
# Insert username and password into dataEx5.db
@app.route("/form_submit5", methods=['POST'])
def submit_form5():
    # Get values
    user = flask.request.form['user']
    password = flask.request.form['password']
    # Insert into table for Example 5
    # The exploit command drops the users table for the dataEx5.db file
    connection = sqlite3.connect('dataEx5.db')
    c = connection.cursor()
    c.executescript("INSERT INTO users (username, password) VALUES ('{0}', '{1}')".format(user, password))
    connection.commit()
    return flask.render_template("create.html")


if __name__ == '__main__':
    # Start server
    app.run(port=5503, host='127.0.0.1', debug=True, use_evalex=False)
