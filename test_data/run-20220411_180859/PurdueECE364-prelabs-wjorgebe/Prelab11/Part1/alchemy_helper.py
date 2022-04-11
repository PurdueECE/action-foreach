# ######################################################
#   Author :    William Jorge
#   email :     wjorgebe@purdue.edu
#   ID :        ee364b12   
#   Date :      April 3, 2022
# ######################################################

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///data/database.db', echo=True)
Session = sessionmaker(bind=engine)
class AlchemyStudent(Base):
    __tablename__ = 'students'
    
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)

def insertStudent(student1, session):
    session.add(student1)
    session.commit()

def removeStudent(student1, session):
    session.delete(student1)
    session.commit()

session = Session()
new_student = AlchemyStudent(first_name='Foo', last_name='Bar', id=4, email='bar.foo@university.com')
insertStudent(new_student, session)
removeStudent(new_student, session)
session.close()
