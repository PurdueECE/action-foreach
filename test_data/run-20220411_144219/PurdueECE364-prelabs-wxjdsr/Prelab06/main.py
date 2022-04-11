# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Feb 12, 2022
# ######################################################
import flask
import sqlite3

app = flask.Flask(__name__)
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
# Q1
@app.route("/create", methods=['GET','POST'])
def create():
	return flask.render_template("form.html")


# Q1 Helper function:
# This function adds the data tuple @task into @conn.
def _insert_data(conn, task):
    sql = ''' INSERT INTO employees(first_name, last_name, id, position)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


# Q1 Add data into database
@app.route("/form_submit", methods=['POST'])
def submit_form():
    # Get data
    first_name = flask.request.form['fname']
    last_name = flask.request.form['lname']
    id = flask.request.form['id']
    position = flask.request.form['position']
    # Insert data into database
    conn = sqlite3.connect('data/company.db')
    task = (first_name, last_name, id, position)
    _insert_data(conn, task)
	# return "Thank you for submitting the form"
    return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name)


# Q2
@app.route("/view", methods=['GET','POST'])
def view_employee_by_id():
    # Link the database
    conn = sqlite3.connect('data/company.db')
    # Find the employee
    c = conn.cursor()
    target_id = flask.request.args.get('emp_id', type = int)
    fetchall = c.execute("SELECT * from employees")
    data_list = fetchall.fetchall()
    first_name = ""
    last_name = ""
    position = ""
    for data in data_list:
        if int(data[2]) == target_id:
            first_name = data[0]
            last_name = data[1]
            position = data[3]
            break

    return flask.render_template('view_by_id.html', first_name = first_name, last_name = last_name, position = position)


# Q2 Helper function:
# This function deletes the data tuple @task into @conn.
def _delete_data(conn, id):
    sql = "DELETE FROM employees where id = '%d'" %id
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    return cur.lastrowid

# Q2 Delete data from database
@app.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    # Get data
    print(flask.request.form)
    first_name = flask.request.form['fname']
    last_name = flask.request.form['lname']
    # first_name = "lll"
    # last_name = "www"
    # id = 61889
    # Insert data into database
    conn = sqlite3.connect('data/company.db')
    _delete_data(conn, id)
	# return "Thank you for submitting the form"
    return flask.render_template('thank_you.html', first_name = first_name, last_name = last_name)


# @app.route("/view/<int:id>", methods=['GET','POST'])
# def view_employee_by_id_dynamic(id):
#     id = None
    

# This block is optional and is used for testing .
# ######################################################
if __name__ == '__main__':
	# Start the server
	app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)