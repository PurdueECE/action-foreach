import flask
import sqlite3

app = flask.Flask(__name__)


@app.route("/create", methods=['GET', 'POST'])
def create():  # URL: http://127.0.0.1:8001/create
    return flask.render_template("form.html")


@app.route("/create_submit", methods=['POST'])
def create_submit():
    username = flask.request.form['username']
    password = flask.request.form['password']

    con = sqlite3.connect('Q3/database.db')
    cur = con.cursor()

    results = cur.execute("SELECT * FROM users where username = " + username + " and password = " + password)
    # results = cur.executescript("SELECT * FROM users where username = " + username + " and password = " + password)

    con.commit()

    db = []
    db.append(["SELECT * FROM users where username = " + username + " and password = " + password])

    for element in (results.fetchall()):
        db.append([element[0], element[1]])

    return flask.render_template('view.html', data=db)


if __name__ == '__main__':
    # Start the server
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)
