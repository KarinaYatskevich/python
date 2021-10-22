from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///homework.db")
base = declarative_base()
session = sessionmaker(bind=engine)()


class Book(base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    page = Column(Integer)

    def __init__(self, name, page):
        self.name = name
        self.page = page



class Students(base):
    __tablename__ = 'studentss'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    book = Column(String, ForeignKey('book.name', ondelete='set null'), nullable=True)

    def __init__(self, first_name, last_name, book):
        self.first_name = first_name
        self.last_name = last_name
        self.book = book



base.metadata.drop_all(engine)  # drop all tables
base.metadata.create_all(engine)  # create all tables

b1 = Book('Python', 140)
b2 = Book('PHP', 180)
b3 = Book('Java', 155)
b4 = Book('JS', 200)
b5 = Book('html', 210)

session.add_all([b1, b2, b3, b4, b5])
session.commit()


s1 = Students(first_name = 'Karina', last_name = 'Yatskevich', book=b1.name)
s2 = Students(first_name = 'marina', last_name = 'Yatskevich', book=b2.name)
s3 = Students(first_name = 'Valeria', last_name = 'Yatskevich', book=b3.name)
s4 = Students(first_name = 'Alex', last_name = 'Yatskevich', book=b4.name)
s5 = Students(first_name = 'Alex', last_name = 'Yatskevich', book=b4.name)

session.add_all([s1, s2, s3, s4, s5])
session.commit()


results = session.query(Students, Book).join(Book, Students.book == Book.name).filter(Students.first_name == 'Alex').all()
for res in results:
    print(f'id:{res.Students.id}, name: {res.Students.first_name}, book: {res.Book.name}')

