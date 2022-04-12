#######################################
# Author: Aedan Frazier
# Email : frazie35@purdue.edu
# ID    : ee364a06
# Date  : 3/10/2022
########################################


import flask
import sqlite3


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template('login.html')


@app.route("/create", methods=['POST'])
def create():
    username = flask.request.form['login']
    password = flask.request.form['password']
    quote = flask.request.form['quote']
    sqlconnect = sqlite3.connect('data/users.db')
    cursor = sqlconnect.cursor()
    cursor.execute("select * FROM users")
    users = dict()
    users = cursor.fetchall()
    print(users)
    i = 0
    user = None
    for u in users:
        if(username in u[0]):
            i = 1
            user = u
            break
    if(i == 0):
        print("Not In Database")
        command = "INSERT INTO users (username, password, quote) VALUES ("
        command = command + "'{}', '{}', ".format(username, password)
        command = command + "'{}');".format(quote)
        cursor.execute(command)
        sqlconnect.commit()
        return flask.render_template('login.html')
    else:
        print("In Database")
        if (user[1] == password):
            print("Correct Password")
            command = "UPDATE users SET quote = '{}' ".format(quote)
            command = command + "WHERE username = '{}'".format(username)
            cursor.execute(command)
            sqlconnect.commit()
            return flask.render_template('login.html')
        else:
            print("Incorrect Password")
            return flask.render_template('login_fail.html')


@app.route("/search", methods=['GET'])
def search():
    username = flask.request.args.get('search')
    sqlconnect = sqlite3.connect('data/users.db')
    cursor = sqlconnect.cursor()
    cursor.execute("SELECT * FROM users WHERE username='{}'".format(username))
    user = dict()
    user = cursor.fetchall()
    sqlconnect.commit()
    print(user)
    values = dict()
    values["Username"] = user[0][0]
    values["Quotes"] = user[0][2]

    return flask.render_template('login_search.html', data=values)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True, use_evalex=False)
