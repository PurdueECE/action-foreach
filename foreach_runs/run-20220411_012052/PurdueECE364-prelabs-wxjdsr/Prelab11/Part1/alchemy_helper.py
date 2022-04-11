# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Apr 3, 2022
# ######################################################

from student import *
from sqlalchemy.orm import declarative_base, sessionmaker, column_property
from sqlalchemy import create_engine, Column, Integer, String
import sqlite3

DATABASE_PATH = "data/database.db"

# SQLAlchemy Setup
Base = declarative_base()
engine = create_engine("sqlite:///" + DATABASE_PATH, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class AlchemyStudent(Base):
    __tablename__ = 'students'
    
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)
    # email = column_property(last_name + "." + first_name + "@university.com")


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
# This helper function converts a Student Class variable
# to an AlchemyStudent Class variable.
def _studentToAlchemyStudent(student1):
    student1_alchemy = AlchemyStudent(
        first_name=student1.firstName, last_name=student1.lastName,
        id=student1.studentID, email=student1.emailID)
    return student1_alchemy


def insertStudent(student1, session):
    # Student -> AlchemyStudent
    student1_alchemy = _studentToAlchemyStudent(student1)
    try:
        session.add(student1_alchemy)
    except sqlite3.IntegrityError as err:
        raise ValueError(f'Student id {student1.studentID} already exists, cannot insert')
    else:
        session.commit()
    
    
def removeStudent(student1, session):
    # Student -> AlchemyStudent
    student1_alchemy = _studentToAlchemyStudent(student1)
    # Find the target and delete
    # It only executes when full match, else nothing happen
    session.query(AlchemyStudent).filter_by(
        first_name=student1.firstName, last_name=student1.lastName,
        id=student1.studentID).delete()
    session.commit()


# ######################################################
# This block is optional and is used for testing .
# ######################################################
# Test the output of database
# new_student = AlchemyStudent(first_name="Xingjian",last_name="Wang",id="316")
# result = session.query(AlchemyStudent).all()
# for row in result:
#    print (row.first_name, row.last_name, row.id, row.email)

# student_sample = Student("Allen", "Chen", 323)
# insertStudent(student_sample, session)
# removeStudent(student_sample, session)