# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 2/19/22 >
# ######################################################
from logging import raiseExceptions
from operator import methodcaller

import os
from pickle import GET
from re import L
import sqlite3 # List of module import statements
import sys
from turtle import position
import flask 
from torch import equal # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
app = flask.Flask(__name__)


@app.route("/create", methods=['GET','POST'])
def create(): #URL: http://127.0.0.1:8001/create
    if flask.request.method == 'POST':
        first_name = flask.request.form['fname']
        last_name = flask.request.form['lname']
        id = flask.request.form['id']
        position = flask.request.form['position']
        with sqlite3.connect('data/company.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO employees (first_name, last_name, id, position) VALUES (?,?,?,?)", 
            (first_name, last_name, id, position))
            connection.commit()
            connection.close()
    # return flask.redirect(flask.url_for('index'))   # Redirect to the index page

    return flask.render_template('form.html')
    

@app.route("/view/<xyz>", methods=['GET', 'POST'])
def emp_id(xyz):
    id = xyz
    if flask.request.method == 'GET': 
        connection = sqlite3.connect("data/company.db")
        cursor = connection.cursor()
        emp_match = (cursor.execute("SELECT first_name, last_name, position from employees where id = ?", (id,)).fetchall())          
        connection.commit()
        cursor.close()
        connection.close()
        return flask.render_template('delete.html', id = id, first_name=emp_match[0][0], last_name=emp_match[0][1], position=emp_match[0][2])

@app.route("/delete", methods=['POST'])
def delete():
    if flask.request.method == 'POST':
        connection = sqlite3.connect("data/company.db")
        
        cursor = connection.cursor()
        id = flask.request.form['id']
        cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
        connection.commit()
        connection.close()
        return "Deleted Successfully!"

@app.route("/view_all", methods=['GET', 'POST'])
def view_all():
    db_list = []
    conn = sqlite3.connect('data/company.db')
    c = conn.cursor()
    fetchall = c.execute("SELECT * from employees")
    for element in (fetchall.fetchall()):
	    db_list.append(element)
	# print(db_dict)
    return flask.render_template('jinja.html', data = db_list)

if __name__ == "__main__":
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)