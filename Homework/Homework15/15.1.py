from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///homework.db")
base = declarative_base()
session = sessionmaker(bind=engine)()


class Prod(base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    comment = Column(String)


base.metadata.drop_all(engine)  # drop all tables
base.metadata.create_all(engine)  # create all tables


prod1 = Prod(name='Pasta', price=5, quantity=1, comment='good')
prod2 = Prod(name='meat', price=7, quantity=2, comment='okay')


session.add_all([prod1, prod2])
session.commit()

# Read
db_prod_1 = session.query(Prod).get(1)
db_prod_2 = session.query(Prod).get(2)

print(db_prod_1.name)
print(db_prod_2.name)


# Update
db_prod_2.price = '10'

session.add(db_prod_2)
session.commit()

db_prod_2 = session.query(Prod).get(2)

print(db_prod_2.price)


# Delete
session.delete(db_prod_2)
session.commit()

db_car_2 = session.query(Prod).get(2)

print(db_prod_2)

