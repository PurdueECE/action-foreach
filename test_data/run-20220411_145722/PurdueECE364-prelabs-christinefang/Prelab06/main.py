import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/create", methods=['GET','POST'])
def create(): #URL: http://127.0.0.1:5000/create
    if flask.request.method == 'POST':
        first_name = flask.request.form['first_name']
        last_name = flask.request.form['last_name']
        id1 = flask.request.form['id']
        position = flask.request.form['position']
        conn = sqlite3.connect('data/company.db')
        c = conn.cursor()
        sql = """INSERT INTO employees (first_name,last_name,id,position)
                VALUES (?,?,?,?)"""
        curr = c.execute(sql,(first_name,last_name,id1,position))
        conn.commit()
        return "Thank you for submitting the form"
    else:
        return flask.render_template("form.html")

@app.route("/view/emp_id=xyz", methods=['POST','GET'])
def view_emp_id_xyz(): #URL: http://127.0.0.1:5000/view/emp_id=xyz
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    fetchall = c.execute("SELECT * from employees")
    for i in (fetchall.fetchall()):
        first_name = i[0]
        last_name = i[1]
        id1 = i[2]
        position = i[3]
        if id1 == 'xyz':
            if flask.request.method == 'POST':
                c.execute("DELETE FROM employees WHERE ID = '{}'".format(id1))
                conn.commit()
                return "thanks"
            return flask.render_template("xyz.html", first_name = first_name, last_name = last_name, id = id1, position = position)
    return "thanks"

@app.route("/view/emp_id/<xyz>", methods=['POST','GET'])
def view_emp_id(xyz): #URL: http://127.0.0.1:5000/view/emp_id=xyz
    id = int(xyz)

    if flask.request.method == "GET":
        conn = sqlite3.connect('data/company.db')
        cur = conn.cursor()
        emp_id = (cur.execute('SELECT first_name,last_name, position from employees where id = ?', (id,)).fetchall())
    return flask.render_template('empid.html',first_name = emp_id[0][0], last_name = emp_id[0][1],id = id, position = emp_id[0][2])

@app.route("/delete",methods = ['POST'])
def delete():
    if flask.request.method == 'POST':
        conn = sqlite3.connect("data/company.db")
        cur = conn.cursor()
        id = flask.request.form['id']
        cur.execute("DELETE FROM employees WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return "Deleted"


@app.route("/view_all", methods=['POST','GET'])
def view_all(): #URL: http://127.0.0.1:5000/view/emp_id=xyz
    db_dict = []
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    fetchall = c.execute("SELECT * from employees")
    for element in (fetchall.fetchall()):
        db_dict.append(element)
    return flask.render_template("list.html", data = db_dict)

if __name__ == '__main__':
	# Start the server
	app.run(port=5000, host='127.0.0.1', debug=True, use_evalex=False)