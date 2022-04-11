from student import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, insert, Table, MetaData
Base = declarative_base()


class AlchemyStudent(Base):
    __tablename__ = 'students'
    firstName = Column(String)
    lastName = Column(String)
    id = Column(Integer, primary_key = True)
    email = Column(String)

def insertStudent(student1, session):
    x = AlchemyStudent(firstName=f"{student1.firstName}",lastName=f"{student1.lastName}", id=f"{student1.studentID}", email=f"{student1.emailID}")
    session.add(x)
    session.commit()
    #stmt = students.insert().values(firstName=f'{student1.firstName}', lastName=f"{student1.lastName}", id = student1.studentID, email = f"{student1.emailID}")
    #conn = engine.connect()
    #res = conn.execute(stmt)
def removeStudent(student1, session):
    session.query(AlchemyStudent).filter_by(id=f"{student1.studentID}").delete()
    session.commit()
    #stmt = students.delete().where(students.c.id == student1.studentID)
    #conn = engine.connect()
    #res = conn.execute(stmt)

if __name__ == "__main__":
    engine = create_engine('sqlite:///data/database.db', echo=True) # Creating engine
    Session = sessionmaker(bind=engine) # Binding it to engine
    Session.configure(bind=engine)
    session = Session() # Instantiate a session
    students = Table(
   'students', MetaData(), 
   Column('firstName', String),
   Column('lastName', String),
   Column('id', Integer, primary_key = True), 
   Column('email', String), 
)
    student1 = Student("Spongebob", "Squarepants",000)
    #insertStudent(student1, session)
    removeStudent(student1, session)
    




