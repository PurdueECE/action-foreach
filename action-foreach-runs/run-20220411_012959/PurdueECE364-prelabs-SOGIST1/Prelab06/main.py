import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/home')
def hello_world():
    return 'Hello, World!'

@app.route("/create", methods=['GET', 'POST'])
def create():
    return flask.render_template('form.html')

@app.route("/create_submit", methods=['POST'])
def create_submit():
    # get results from form
    first_name = flask.request.form['first_name']
    last_name  = flask.request.form['last_name']
    ID         = flask.request.form['id']
    position   = flask.request.form['position']
    # print them for viewability
    print(first_name)
    print(last_name)
    print(ID)
    print(position)
    # put them into the database
    #db_dict = {"first_name":first_name, "last_name":last_name, "ID":ID, "position":position} # put variables in a dictionary
    conn = sqlite3.connect('data/company.db') # open the database
    conn.execute("INSERT INTO employees (first_name, last_name, id, position) VALUES(?,?,?,?)",(first_name,last_name,ID,position))
    conn.commit()
    conn.close() # close the database
    return flask.render_template('form_submit.html', first_name = first_name, last_name = last_name, id = ID, position = position) # show finished form results to user

@app.route("/view", methods=['GET', 'POST'])
def view():
    args = flask.request.args
    print(args)
    conn = sqlite3.connect('data/company.db') # open the database
    c = conn.cursor()
    employee = (c.execute("SELECT first_name,last_name,id,position FROM employees WHERE id = ?",(args["emp_id"],)).fetchall())
    print(conn.row_factory)
    conn.close() # close the database
    first_name = employee[0][0]
    last_name  = employee[0][1]
    ID         = employee[0][2]
    position   = employee[0][3]
    db_dict = {"Full name":first_name + ' ' + last_name, "Position":position} # put variables in a dictionary
    print(db_dict)
    return flask.render_template('view.html', data = db_dict, id = ID)

@app.route("/view_delete", methods=['POST'])
def view_delete():
    args = flask.request.args # get the id from the arguments
    print('delete view args:')
    print(args["emp_id"])
    conn = sqlite3.connect('data/company.db') # open the database
    conn.execute("DELETE FROM employees WHERE id = ?",(args["emp_id"],)) # delete employee from database
    conn.commit()
    conn.close() # close the database
    message = "Successfully deleted employee ID: "+args["emp_id"] # delete success message
    return message

@app.route("/view/<emp_id>", methods=['GET', 'POST'])
def id_view(emp_id):
    conn = sqlite3.connect('data/company.db') # open the database
    c = conn.cursor()
    employee = (c.execute("SELECT first_name,last_name,id,position FROM employees WHERE id = ?",(emp_id,)).fetchall())
    conn.close() # close the database
    first_name = employee[0][0]
    last_name  = employee[0][1]
    ID         = employee[0][2]
    position   = employee[0][3]
    db_dict = {"Full name":first_name + ' ' + last_name, "Position":position} # put variables in a dictionary
    print(db_dict)
    return flask.render_template('view.html', data = db_dict, id = ID)

@app.route("/view_all", methods=['GET', 'POST'])
def view_all():
    conn = sqlite3.connect('data/company.db') # open the database
    c = conn.cursor()
    employee = (c.execute("SELECT * FROM employees").fetchall())
    conn.close() # close the database
    print('viewall:')
    print(employee)
    db_dict = {}
    i = 1
    for employee_info in employee:
        db_dict["Employee " + str(i)] = employee_info[0] + ' ' + employee_info[1] + ', ' + employee_info[3]
        i += 1
    return flask.render_template('view_all.html', data = db_dict)

if __name__ == "__main__":
    #start the server
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)