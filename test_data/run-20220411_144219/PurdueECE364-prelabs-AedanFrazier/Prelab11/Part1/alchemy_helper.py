########################################
# Author:   Aedan Frazier
# Email:    frazie35@purdue.edu
# ID:       ee364a06
# Date:     3/28/2022
########################################

from student import * 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()

def insertStudent(student1: Student, session):
    stu = AlchemyStudent(first_name=student1.firstName, last_name=student1.lastName, id=student1.studentID, email=student1.emailID)
    session.add(stu)
    session.commit()


def removeStudent(student1: Student, session):
    session.query(AlchemyStudent).filter(AlchemyStudent.id==student1.studentID).\
    delete(synchronize_session=False)
    session.commit()

class AlchemyStudent(Base):
    __tablename__ = "students"
    first_name  = Column(String)
    last_name   = Column(String)
    id          = Column(Integer, primary_key = True)
    email       = Column(String)

if __name__ == "__main__":
    engine = create_engine('sqlite:///data/database.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    George = Student(firstName="George", lastName="Lopez", studentID=987987987)
    #insertStudent(George, session)
    #removeStudent(George, session)
