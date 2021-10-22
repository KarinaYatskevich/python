from sqlalchemy.orm import sessionmaker
from first import *
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test3.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

person_one = Book(name_book='python')
session.add(person_one)
session.commit()

session.add_all([Person(firstname='karina', lastname='yatskevich', phone='4645')])
session.commit()









# session.add(Person('Alex', 'Varkalov', 123, 'fjyfvjf'))
# session.add_all([Person('Alex', 'Petrov', 565, 'gfjf'), Person('Ann', 'Ivanova', 4654, 'hygjhyg')])
# session.add(Book('jfjdkskskskksksk'))
# session.commit()