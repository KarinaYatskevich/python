from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///test3.db", echo=True)
Base = declarative_base()

class Person(Base):

 __tablename__ = 'person'
 id = Column(Integer, primary_key=True)
 firstname = Column(String)
 lastname = Column(String)
 phone = Column(Integer)
 book = relationship('Book')


class Book(Base):
 __tablename__ = 'book'
 id = Column(Integer, primary_key=True)
 name_book = Column(String(250))

Base.metadata.create_all(engine)


# def __init__(self, firstname, lastname, phone, book):
#  self.firstname = firstname
#  self.lastname = lastname
#  self.phone = phone
#  self.book = book

# def __init__(self, name_book):
#  self.name_book = name_book