from flask import Flask, render_template, request
import sqlite3 as db

app = Flask(__name__)


def addEmployee(f, last, id, p):
    conn = db.connect("data/company.db")
    c = conn.cursor()
    query = f'INSERT INTO users VALUES("{f}", "{last}", "{id}", "{p}")'
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()


def getEmployeeByID(id, p):
    conn = db.connect("data/company.db")
    c = conn.cursor()
    query = f'SELECT * FROM users WHERE username="{id}" AND password="{p}"'
    print(f"\tSQL QUERY: {query}")
    data = c.execute(query).fetchall()[0]
    c.close()
    conn.close()
    return data


@app.route("/")
def homeLogin():
    return render_template("login.html")


@app.route("/handle", methods=["GET", "POST"])
def handleLoginReq():
    id = request.form['userid']
    data = getEmployeeByID(id, request.form['password'])
    return f"{data}"


@app.route("/a")
def addUser():
    return render_template("form.html")


@app.route("/h", methods=["POST"])
def handleAddUser():
    addEmployee(request.form["firstname"], request.form["lastname"],
                request.form["username"], request.form["password"])
    return "Thank you believeing in us"


if __name__ == "__main__":
    app.run(port=5001, host='127.0.0.1', debug=True, use_evalex=False)
