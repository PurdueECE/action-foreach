import flask
import sqlite3

app = flask.Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./data/company.db')
    c = conn.cursor()
    try:
        c.execute("CREATE TABLE IF NOT EXISTS employee (fname TEXT, lname TEXT, ID INTEGER, Pos TEXT)")
    except:
        pass
    return conn

@app.route("/", methods=['GET', 'POST'])
def bas():
    conn = get_db_connection()
    conn.close()
    return flask.render_template('intro.html')

@app.route("/create", methods=['GET', 'POST'])
def create():
    return flask.render_template('form.html')

@app.route("/create2", methods=['GET', 'POST'])
def create2():
    lname = flask.request.form.get("firstname")
    fname = flask.request.form.get("lastname")
    id = flask.request.form.get("ID")
    pos = flask.request.form.get("position")
    
    conn = sqlite3.connect('./data/company.db')
    c = conn.cursor()
    c.execute("INSERT INTO employee (fname, lname, ID, Pos) VALUES (?, ?, ?, ?)", (fname, lname, id, pos))
    #c.execute("INSERT INTO employee (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()
    c.close()
    return flask.render_template('add.html')
if __name__ == '__main__':
    app.run(debug=True)