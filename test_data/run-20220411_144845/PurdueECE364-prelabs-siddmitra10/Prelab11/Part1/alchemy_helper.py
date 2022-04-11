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
    first_name = student1.firstName
    last_name = student1.lastName
    id = int(student1.studentID)
    email = student1.emailID
    x = AlchemyStudent(first_name=f"{first_name}",last_name=f"{last_name}", id=id, email=f"{email}")
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
    mom = Student("Anu", "Mitra", 15)
    sidd = Student("Sidd", "Mitra", 100)
    students = Table("students", MetaData(), Column("first_name", String), Column("last_name", String), Column("id", Integer, primary_key=True), Column("email", String))
    # insertStudent(mom, session)
    insertStudent(sidd, session)
    # removeStudent(sidd, session)