# ######################################################
# Author : Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : 04/03/2021
# ######################################################
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class AlchemyStudent(Base):
    __tablename__ = 'students'
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)

    def __init__(self,first_name,last_name,id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.email = self.last_name + '.' + self.first_name + '@university.com'
    
    def insertStudent(student1, session):
        session.add(student1)
        session.commit()

    def removeStudent(student1, session):
        session.delete(student1)
        session.commit()

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db', echo=True)
    Session = sessionmaker(bind=engine)()

    student1 = AlchemyStudent("person","p1","334")
    # AlchemyStudent.insertStudent(student1, Session)
    studentdel = Session.query(AlchemyStudent).filter(AlchemyStudent.id=="123").first()
    AlchemyStudent.removeStudent(studentdel, Session)
    