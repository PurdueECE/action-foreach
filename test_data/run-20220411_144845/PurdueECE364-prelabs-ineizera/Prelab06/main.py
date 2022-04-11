from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('data/company.db')
c = connection.cursor()
c.execute('DROP TABLE IF EXISTS employees;')
c.execute('CREATE TABLE employees (first_name TEXT, last_name TEXT, id INTEGER PRIMARY KEY, position TEXT);')
c.close()

@app.route("/", methods=['GET', 'POST'])
def home():
    return redirect("http://127.0.0.1:8001/create")

@app.route("/create", methods=['GET', 'POST'])
def create():
    return render_template("create.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            first_name = request.form['fname']
            last_name = request.form['lname']
            id = request.form['id']
            position = request.form['position']

            connection = sqlite3.connect('data/company.db')
            c = connection.cursor()
            c.execute('INSERT INTO employees (first_name, last_name, id, position) VALUES (?, ?, ?, ?)', (first_name, last_name, id, position))
            msg = "Succesfully added new employee to company database!"
            connection.commit()
                
        except:
            msg = "Error! Failed to add new employee to company database..."
            connection.rollback()

        finally:
            c.close()
            return render_template("result.html", msg = msg)

@app.route("/view", methods=['GET', 'POST'])
@app.route("/view/<emp_id>", methods=['GET', 'POST'])
def view(emp_id=None):
    if emp_id is None:
        id = request.args.get('emp_id')
    else:
        id = emp_id

    connection = sqlite3.connect('data/company.db')
    connection.row_factory = sqlite3.Row
    c = connection.cursor()
    c.execute("SELECT * FROM employees WHERE id = ?", (id,))
    rows = c.fetchall(); 
    c.close()
    return render_template("view.html", rows = rows, emp_id = id)

@app.route("/delete/<emp_id>", methods=['GET', 'POST']) 
def delete(emp_id):
    id = emp_id
    connection = sqlite3.connect("data/company.db")
    connection.row_factory = sqlite3.Row
    c = connection.cursor()
    c.execute("DELETE FROM employees WHERE id = ?", (id,))
    connection.commit()
    msg = "The employee was deleted."
    c.close()
    return render_template("delete.html", msg=msg)

@app.route("/view_all", methods=['GET', 'POST']) 
def viewall():
    connection = sqlite3.connect("data/company.db")
    connection.row_factory = sqlite3.Row
    c = connection.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall(); 
    c.close()
    return render_template("viewall.html", rows = rows)

if __name__ == '__main__':
    #Start the server
    app.run(port=8001, host='127.0.0.1', debug=True)