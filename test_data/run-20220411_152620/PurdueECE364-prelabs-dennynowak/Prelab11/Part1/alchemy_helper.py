################################
#   Author: Denny Nowak
#   Email:  nowak32@purdue.edu
#   ID:     ee364b14
#   Date:   04/02/2022
################################
import student
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
Base = declarative_base()


# Alchemy Student class with students table
class AlchemyStudent(Base):
    __tablename__ = 'students'
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)


# Insert new row into students table
def insertStudent(student1, session):
    student = AlchemyStudent(first_name=str(student1.firstName), last_name=str(student1.lastName), id=int(student1.studentID), email=str(student1.getEmailID()))
    session.add(student)
    session.commit()


# Delete row from students table
def removeStudent(student1, session):
    student = AlchemyStudent(first_name=str(student1.firstName), last_name=str(student1.lastName), id=int(student1.studentID), email=str(student1.getEmailID()))
    session.query(AlchemyStudent).filter_by(first_name=str(student1.firstName), last_name=str(student1.lastName), id=int(student1.studentID), email=str(student1.getEmailID())).delete()
    session.commit()


if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Testing
    # testStudent = student.Student('student1', 'test1', 1)
    # insertStudent(testStudent, session)
    # testStudent2 = student.Student('student2', 'test2', 2)
    # insertStudent(testStudent2, session)
    # removeStudent(testStudent, session)
    session.close()
