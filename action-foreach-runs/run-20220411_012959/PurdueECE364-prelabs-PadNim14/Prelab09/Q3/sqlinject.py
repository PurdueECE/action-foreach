# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 3/10/22 >
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
import uuid
from torch import equal # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
app = flask.Flask(__name__)


@app.route("/login", methods=['GET','POST'])
def login(): #URL: http://127.0.0.1:8001/create
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        id = uuid.uuid1()
        with sqlite3.connect('data/users.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password, id) VALUES (?,?,?)", 
            (username, password, str(id)))
            cursor.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password))
            test = cursor.fetchone()
            print(test[1])
            if "--" in test[1] or "' OR 1=1" in test[1] or """=""" in test[1] or "" in test[1]:
                return "You've been attacked " + str(test[1])
        #  The SQL attacks are in the database.
    return flask.render_template('form.html')


@app.route("/view/<xyz>", methods=['GET', 'POST'])
def emp_id(xyz):
    id = xyz
    if flask.request.method == 'GET': 
        connection = sqlite3.connect("data/users.db")
        cursor = connection.cursor()
        emp_match = (cursor.execute("SELECT username, password from users where id = ?", (id,)).fetchall())          
        connection.commit()
        cursor.close()
        connection.close()
        return flask.render_template('delete.html', id = id, username=emp_match[0][0], password=emp_match[0][1])

@app.route("/delete", methods=['POST'])
def delete():
    if flask.request.method == 'POST':
        connection = sqlite3.connect("data/users.db")
        
        cursor = connection.cursor()
        id = flask.request.form['id']
        cursor.execute('DELETE FROM users WHERE id = ?', (id,))
        connection.commit()
        connection.close()
        return "Deleted Successfully!"

@app.route("/view_all", methods=['GET', 'POST'])
def view_all():
    db_list = []
    conn = sqlite3.connect('data/users.db')
    c = conn.cursor()
    fetchall = c.execute("SELECT * from users")
    for element in (fetchall.fetchall()):
	    db_list.append(element)
	# print(db_dict)
    return flask.render_template('jinja.html', data = db_list)

if __name__ == "__main__":
    app.run(port=3001, host='127.0.0.1', debug=True, use_evalex=False)