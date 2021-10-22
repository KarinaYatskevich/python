from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

engine = create_engine("sqlite:///l_17.02.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Departament(Base):
    __tablename__='departament'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class Employer(Base):
    __tablename__='employer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class DepEmp(Base):
    __tablename__ = 'employer_to_departure'
    employer_id = Column(Integer, ForeignKey('employer_id', ondelete='no action'), primary_key=True)
    departament_id = Column(Integer, ForeignKey('departament_id', ondelete='cascade'), primary_key=True)

    def __init__(self, employer_id, department_id):
        self.employer_id = employer_id
        self.departament_id = department_id


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()

e1 = Employer('Karina', 'Yatskevich')
d1 = Departament('d1')

session.add_all([e1, d1])

session.commit()

session.add(DepEmp(e1.id, d1.id))
session.commit()