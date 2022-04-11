from flask import Flask, redirect, render_template, request
from db import addEmployee, getEmployeeByID
from db import deleteEmployeeByID, getAllEmployees

app = Flask(__name__)

@app.route("/handle", methods=["POST"])
def handle():
    addEmployee(request.form['first_name'], request.form['last_name'], request.form['id'], request.form['position'])
    return f"<h1>Thank you for filling out the form Mr./Mrs. {request.form['last_name']}</h1>"

@app.route("/create")
def form():
    return render_template("form.html")

@app.route("/view")
def view():
    id = request.args['emp_id']
    employee = getEmployeeByID(id)
    return render_template("employeeInfo.html", first_name=employee[0], last_name=employee[1], id=employee[2], position=employee[3])

@app.route("/view/<int:id>")
def view2(id):
    employee = getEmployeeByID(id)
    return render_template("employeeInfo.html", first_name=employee[0], last_name=employee[1], id=employee[2], position=employee[3])

@app.route("/delete", methods=["POST"])
def delete():
    deleteEmployeeByID(request.form['id'])
    return f"User {request.form['id']} has been deleted"


@app.route("/view_all")
def viewAll():
    employees = getAllEmployees()
    return render_template("fullList.html", employees=employees)


if __name__ == "__main__":
    app.run(port=5001, host='127.0.0.1', debug=True, use_evalex=False)
