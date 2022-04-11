from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from student import Student


Base = declarative_base()

class AlchemyStudent(Base):
    __tablename__ = "students"
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    email = Column(String)

    
def insertStudent(student1, session):
    s1 = student1.firstName
    s2 = student1.lastName
    s3 = student1.studentID
    s4 = student1.emailID
    x = AlchemyStudent(first_name=f"{s1}",last_name=f"{s2}", id=f"{s3}", email=f"{s4}")
    session.add(x)
    session.commit()


def removeStudent(student1, session):
    session.query(AlchemyStudent).filter_by(id=f"{student1.studentID}").delete()
    session.commit()
    
if __name__ == "__main__":
    engine = create_engine("sqlite:///data/database.db", echo=True)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()
    ishaan = Student("Ishaan", "Jain", 457)
    students = Table("students", MetaData(), Column("first_name", String), Column("last_name", String), Column("id", Integer, primary_key=True), Column("email", String))
    #insertStudent(ishaan, session)
    removeStudent(ishaan, session)