import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/create", methods=['GET','POST'])
def create():
    db_dict = {}
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    conn.close()
    return flask.render_template('create.html',data=db_dict)

@app.route("/view_all", methods=['GET','POST'])
def view_all():
    employeelist = []
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    fetchall = c.execute("SELECT * from employees").fetchall()
    for element in (fetchall):
    	print(element)
    	employeelist.append([element[0],element[1],element[3]])
    print (fetchall)
    conn.close()
    return flask.render_template('view_all.html', data = employeelist)

@app.route("/view/", methods=['GET','POST'])
def view_specific():
    emp_id = flask.request.args.get('emp_id')
    print(emp_id)
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    employee = c.execute("SELECT first_name,last_name,position FROM employees WHERE id = (?)", [emp_id]).fetchone()
    print(employee)
    message = f"{employee[0]} {employee[1]} {employee[2]}"
    conn.close()
    return flask.render_template('view_one.html', element = employee)

@app.route("/form_submit", methods=['POST'])
def submit_form():
    db_dict = {}
    first_name = flask.request.form['first_name']
    last_name = flask.request.form['last_name']
    idbad = flask.request.form['id']
    position = flask.request.form['position']
    print(first_name)
    print(last_name)
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (first_name, last_name, id, position) VALUES (?,?,?,?)",(first_name, last_name, idbad, position))
    conn.commit()
    conn.close()
    return flask.render_template('submitted.html')

if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)