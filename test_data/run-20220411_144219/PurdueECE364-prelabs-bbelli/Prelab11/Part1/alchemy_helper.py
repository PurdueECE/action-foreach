import sqlalchemy
from sqlalchemy.orm import declaretive_base
from sqlalchemy import create_engine

Base = declaretive_base()
engine = create_engine('database.db', echo=True)

class AlcehmyStudent(Base):
    __tablename__ = 'students'

    name = Column(String)
    lname = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)
    
    def __repr__(self):
        return "<User(name='%s', lname='%s', email'%s')>" % (
                            self.name, self.lname, self.email)

def instertStudent(student1, session):




def removeStudent(student1, session):
    



