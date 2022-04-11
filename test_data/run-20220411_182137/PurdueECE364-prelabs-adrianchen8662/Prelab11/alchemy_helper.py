from sqlalchemy.orm import declarative_base, sessionmater
from sqlalchemy import Column, Integer, String, create_engine
import student.py

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    firstname = Column(String)
    lastname = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)

    session = sessionmaker(bind=engine)

    def insertStudent(student1, session):
        student = Student(firstname=student1.firstName,lastname=student1.lastName,id=student1.studentID,email=student1.emailID)
        session.add(student)
        
    def removeStudent(student1, session):
        session.delete(session.query(Student).filter_by(firstName=student1.firstName,lastname=student1.lastname,id=student1.studentID, email=student1.emailID))
