# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Mar 11, 2022
# ######################################################
import flask
import sqlite3

app = flask.Flask(__name__)


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
@app.route("/create", methods=['GET', 'POST'])
def create():
    return flask.render_template("homepage.html")


# Q3 Helper function:
# This function selects @data from @conn.
# @pre: Every username is unique
# @return: True if username and password is found, else False
def _select_data(conn, data):
    # data[0] is username and data[1] is password
    c = conn.cursor()
    # SQL statement with problems:
    # sql = ' SELECT * FROM user_info WHERE username ="' + data[0] \
    #     + '" AND password ="' + data[1] + '"'
    # SQL parameters that prevents SQL injection:
    sql_parameter = {'username': data[0], 'password': data[1]}
    sql = "SELECT * FROM user_info WHERE username = '%(username)s' \
        AND password = '%(password)s'" % sql_parameter
    # print(sql)    # See the printout in console
    fetchall = c.execute(sql).fetchall()
    return True if fetchall else False


@app.route("/create_success", methods=['POST'])
def submit_form():
    username = flask.request.form['username']
    password = flask.request.form['password']
    # Select data from database
    conn = sqlite3.connect('data/user.db')
    data = (username, password)
    is_matched = _select_data(conn, data)
    response_page = ""
    # If the username and password is matched, return "Welcome" page
    # Else, return "username or password is not found"
    if is_matched:
        response_page = flask.render_template('welcome.html',
                                              username=username)
    else:
        response_page = flask.render_template('error_info.html')
    return response_page


# This block is optional and is used for testing .
# ######################################################
if __name__ == '__main__':
    # Start the server
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)
