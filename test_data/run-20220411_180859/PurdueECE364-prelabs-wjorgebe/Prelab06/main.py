from email import message
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/create", methods=['GET', 'POST'])
def form():
    return flask.render_template("form.html")

@app.route("/form_submit", methods=['POST'])
def submit_form():
    first_name = flask.request.form['fname']
    last_name = flask.request.form['lname']
    id = flask.request.form['id']
    position = flask.request.form['position']
    create_employee(first_name, last_name, id, position)
    return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name)

@app.route("/view", methods=['GET', 'POST'])
def employee_display(): 
    id = flask.request.args.get('emp_id')
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    employee = (c.execute("SELECT first_name,last_name,id,position from employees where id = ?", (id,)).fetchall())
    full_name = (employee[0][0], employee[0][1])
    emp_id = employee[0][2]
    position = employee[0][3]
    return flask.render_template('employee.html', first_name=full_name[0], last_name=full_name[1], id=emp_id, pos=position)

@app.route("/view/emp_id/<emp_id>", methods=['GET', 'POST'])
def employee_display_dynamic(emp_id): 
    id = emp_id
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    employee = (c.execute("SELECT first_name,last_name,id,position from employees where id = ?", (id,)).fetchall())
    full_name = (employee[0][0], employee[0][1])
    emp = employee[0][2]
    position = employee[0][3]
    return flask.render_template('employee.html', first_name=full_name[0], last_name=full_name[1], id=emp, pos=position)

@app.route("/emp_delete/<emp_id>", methods=['POST'])
def delete_emp(emp_id):
    DATABASE = 'data/company.db'
    id = emp_id
    conn = sqlite3.connect(DATABASE)
    sql = '''DELETE FROM employees where id = ?'''
    cur = conn.cursor()
    cur.execute(sql, id)
    conn.commit()
    return "The employee has been deleted."

@app.route("/view_all", methods=['GET', 'POST'])
def grocery_alljinja():
	db_dict = {}
	conn = sqlite3.connect('data/company.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from employees")
	for element in (fetchall.fetchall()):
		db_dict.update({element[0] + " " + element[1]: element[3]})
	print(db_dict)
	return flask.render_template('jinjaall.html', data = db_dict)

def create_employee(first_name, last_name, id, position):
    DATABASE = 'data/company.db'
    conn = sqlite3.connect(DATABASE)
    employee_info = (first_name, last_name, id, position)
    sql = '''INSERT INTO employees(first_name, last_name, id, position)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, employee_info)
    conn.commit()
    return

if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)