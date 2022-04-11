import sqlite3

connection = sqlite3.connect('q3_data.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS database
              (name TEXT, lname TEXT, age INT)''')

connection.commit()
connection.close()