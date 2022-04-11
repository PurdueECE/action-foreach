from email import message
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def form():
    return flask.render_template("template.html")


def login(username, password):
    DATABASE = 'data/company.db'
    conn = sqlite3.connect(DATABASE)
    info = (username, password)
    sql = '''SELECT * FROM logins WHERE username = ''' + username # + '''AND password = ''' + password
    cur = conn.cursor()
    cur.execute(sql, info)
    conn.commit()
    return

print("Injection examples:\n")
print("Example #1: See all users in table")
print("  Username: dummy OR 1=1")
print("  SQL Statement: SELECT * FROM logins WHERE username = dummy OR 1=1")
print("Example #2: Table gets deleted")
print("  Username: hello); DROP TABLE logins")
print("  SQL Statement: SELECT * FROM logins WHERE username = hello); DROP TABLE logins")
print("Example #3: Bypass authentication")
print("  Username: "" OR ""="",     Password = "" OR ""=""")
print("  SQL Statement: SELECT * FROM logins WHERE username ="" or ""="" AND password ="" or ""=""")
print("Example #4: Retrieve user password")
print("  Username: williamj,     Password = "" OR ""=""")
print("  SQL Statement: SELECT * FROM logins WHERE username =williamj AND password ="" or ""=""")
print("Example #5: Retrieve data by name")
print("  Username: William      Password: "" OR ""=""); UNION SELECT username, password WHERE name=username);")
print(" . SELECT * FROM logins where username = William AND password= "" OR ""=""); UNION SELECT username, password WHERE name=username);")


if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)