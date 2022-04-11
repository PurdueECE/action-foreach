import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('form.html')

@app.route("/create", methods=['POST'])
def create():
    firstname = flask.request.form['firstname']
    lastname = flask.request.form['lastname']
    pid = flask.request.form['id']
    position = flask.request.form['position']
 
    sqlconnect = sqlite3.connect('data/company.db')
    cursor = sqlconnect.cursor()
    cursor.execute("INSERT INTO employees (first_name, last_name, id, position) VALUES ('{}', '{}', {}, '{}');".format(firstname, lastname, pid, position))
    sqlconnect.commit()
    return flask.render_template('thanks.html')
	
@app.route("/view/<int:emp_id>", methods=['GET'])
def view_employee_dynamic(emp_id):
    sqlconnect = sqlite3.connect('data/company.db')
    cursor = sqlconnect.cursor()
    cursor.execute("SELECT * FROM employees WHERE id={}".format(emp_id))
    employee = dict()
    employee = cursor.fetchall()
    field = ["First Name", "Last Name", "ID", "Position"]
    value = dict()

    for emp in employee:
        i = 0
        for item in emp:
            value[field[i]] = item
            i = i + 1
    return flask.render_template('employee.html', data = value)
    pass

@app.route("/view", methods=['GET'])
def view_employee_static():
    pid = flask.request.args.get('emp_id')
    sqlconnect = sqlite3.connect('data/company.db')
    cursor = sqlconnect.cursor()
    cursor.execute("SELECT * FROM employees WHERE id={}".format(pid))
    employee = dict()
    employee = cursor.fetchall()
    field = ["First Name", "Last Name", "ID", "Position"]
    value = dict()

    for emp in employee:
        i = 0
        for item in emp:
            value[field[i]] = item
            i = i + 1
    return flask.render_template('employee.html', data = value)

@app.route("/delete", methods=['POST'])
def delete_employee():
    pid  = flask.request.form['ID']
    sqlconnect = sqlite3.connect('data/company.db')
    cursor = sqlconnect.cursor()
    cursor.execute("DELETE FROM employees WHERE id={}".format(pid))
    sqlconnect.commit()
    return flask.render_template('deleted.html')

@app.route("/view_all", methods=['GET'])
def view_all():
    sqlconnect = sqlite3.connect('data/company.db')
    cursor = sqlconnect.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = dict()
    employees = cursor.fetchall()
    value = dict()

    for emp in employees:
        value[emp[2]] = emp

    return flask.render_template('employees.html', data = value)

if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)
