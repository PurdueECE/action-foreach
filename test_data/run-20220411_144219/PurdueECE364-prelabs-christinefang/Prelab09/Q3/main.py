import flask
import sqlite3

app = flask.Flask(__name__)


@app.route("/create", methods=['GET', 'POST'])
def create():
    if flask.request.method == 'POST':
        user = flask.request.form['username']
        passw = flask.request.form['password']
        print(user + ' ' + passw)
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        sql = """INSERT INTO users (username, password)
                VALUES (?,?)"""
        c.execute(sql, (user, passw))
        conn.commit()
        return "Thank you for submitting the form"
    else:
        return flask.render_template("form.html")


if __name__ == '__main__':
    # Start the server
    app.run(port=5000, host='127.0.0.1', debug=True, use_evalex=False)
