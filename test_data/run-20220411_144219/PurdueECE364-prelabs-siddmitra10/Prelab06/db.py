import sqlite3 as db

def addEmployee(first_name, last_name, id, position):
    conn = db.connect("data/company.db")
    c = conn.cursor()
    c.execute(f'INSERT INTO employees VALUES("{first_name}", "{last_name}", {id}, "{position}")')
    conn.commit()
    c.close()
    conn.close()

def getEmployeeByID(id):
    conn = db.connect("data/company.db")
    c = conn.cursor()
    data = c.execute(f'SELECT * FROM employees WHERE id={id}').fetchall()[0]
    c.close()
    conn.close()
    return data

def deleteEmployeeByID(id):
    conn = db.connect("data/company.db")
    c = conn.cursor()
    c.execute(f'DELETE FROM employees WHERE id={id}')
    conn.commit()
    c.close()
    conn.close()

def getAllEmployees():
    conn = db.connect("data/company.db")
    c = conn.cursor()
    data = c.execute(f'SELECT * FROM employees').fetchall()
    c.close()
    conn.close()
    return data

    
