from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from Part1.database_helper import insertStudent
from sqlalchemy import insert, delete
# from base import Base
from student import Student


Base = declarative_base()

class AlchemyStudent(Base):
    __tablename__ = "students"
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)

    # def __init__(self, firstName, lastName, studentID):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.studentID = studentID
    #     self.emailID = lastName +"."+ firstName +"@university.com"
    
    
    def __repr__(self):
        return "<AlchemyStudent(first_name='%s', last_name='%s', id='%d, email='%s'')>" % (
                             self.first_name, self.last_name, self.id, self.email)
    
def insertStudent(student1, session):
    # print(f"This is student: {student1.firstName + student1.lastName}")
    # x = students.insert().values(first_name=f"{student1.firstName}",last_name=f"{student1.lastName}", id=f"{student1.studentID}", email=f"{student1.emailID}")
    x = AlchemyStudent(first_name=f"{student1.firstName}",last_name=f"{student1.lastName}", id=f"{student1.studentID}", email=f"{student1.emailID}")
    session.add(x)
    session.commit()


def removeStudent(student1, session):
    session.query(AlchemyStudent).filter_by(id=f"{student1.studentID}").delete()
    session.commit()
    
if __name__ == "__main__":
    engine = create_engine("sqlite:///data/database.db", echo=True)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()
    # session = Session()
    nimal = Student("Nimal", "Padma", 309)
    students = Table("students", MetaData(), Column("first_name", String), Column("last_name", String), Column("id", Integer, primary_key=True), Column("email", String))
    # # print(nimal.firstName)
    # alch = AlchemyStudent("Nimal", "Padma", 3746)
    # insertStudent(nimal, session)
    removeStudent(nimal, session)