import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class AlchemyStudent(Base):
    __tablename__ = 'students'
    # def __init__(self, firstName, lastName, studentID, emailID):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.studentID = studentID
    #     self.emailID = emailID
    firstName = column(String)
    lastName = Column(String)
    studentID = Column(Integer, primary_key=True)
    emailID = Column(String)
    # def __repr__(self):
    #     return "<User(firstName='%s', lastName='%s', emailID='%s')>" % (
    #                 self.firstName, self.lastName, self.emailID)


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#                     self.name, self.fullname, self.nickname)
def insertStudent(student1, session):
    con = sqlalchemy.connect('.. Part1/data/database.db')
    cur = con.cursor()
    firstName = str(student1.firstName)
    lastName = str(student1.lastName)
    studentID = str(student1.studentID)
    emailID = str(student1.emailID)

    cur.execute(f'''INSERT INTO students VALUES 
                    ('{firstName}','{lastName}',
                    '{studentID}','{emailID}')''')
    
    # con.commit()
    # con.close()
    return


def removeStudent(student1, session):
    oldID = student1.studentID
    newStudent1 = student.Student(student1.firstName, student1.lastName, ID, student1.emailID)

    #verify duplicates first
    cur.execute(f'''SELECT id FROM students WHERE id = ('{ID}')''')
    items = cur.fetchall()
    if items:
        print('ID Already Exists!')
        return
    #delete + replace
    cur.execute(f'''DELETE FROM students WHERE id = {oldID}''')
    return

if __name__ == '__main__':
    con = sqlalchemy.connect('.. Part1/data/database.db')
    cur = con.cursor()
    student1 = AlchemyStudent('a','b',1,'c')

    # # cur.execute('''CREATE TABLE students
    # #                 (first_name text, last_name text, 
    # #                 id int primary key, email text)''')

    # student1 = student.Student('a','b',4,'c')
    # # print(student1.firstName, student1.lastName, student1.studentID, student1.emailID)
    # # insertStudent(student1)
    # # getStudentsByName('b')
    # updateID(student1, 5)


    con.commit()
    con.close()