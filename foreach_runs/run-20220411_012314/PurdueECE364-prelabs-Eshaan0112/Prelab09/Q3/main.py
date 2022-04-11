import flask
import sqlite3
app = flask.Flask(__name__)


@app.route("/create", methods=['GET', 'POST'])
def create():
    if flask.request.method == 'POST':
        first_name = flask.request.form['fname']
        last_name = flask.request.form['lname']
        with sqlite3.connect('data/login.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO login_info (Username, Password) VALUES (?, ?)", (first_name, last_name))
            connection.commit()
    return flask.render_template('form.html')


if __name__ == "__main__":
    print("\nQ3 SQL Exploiting Commands:")
    print("INSERT INTO login_info VALUES (Eshaan, Minocha);")  # Example 1
    print("INSERT INTO login_info VALUES (1, 2);")  # Example 2
    print("SELECT * FROM login_info WHERE Username='Eshaan';")  # Exmaple 3
    print("INSERT INTO login_info VALUES (10.0, 9.66666);")  # Example 4
    print("INSERT INTO login_info VALUES ('Eshaan', Minocha);")  # Example 5
    app.run(port=9008, host='127.0.0.1', debug=True, use_evalex=False)
