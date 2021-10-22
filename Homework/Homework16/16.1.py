from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:i2245699@localhost/postgres")
base = declarative_base()
session = sessionmaker(bind=engine)()


class Brand(base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Car(base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand = Column(Integer, ForeignKey('brands.id'))


base.metadata.drop_all(engine)  # drop all tables
base.metadata.create_all(engine)  # create all tables


# Create
brand1 = Brand(name="BMW")
brand2 = Brand(name="Toyota")

session.add_all([brand1, brand2])
session.commit()

car1 = Car(model='X5', release_year=2012, brand=brand1.id)
car2 = Car(model='Camry', release_year=2007, brand=brand2.id)

session.add_all([car1, car2])
session.commit()


# Read
db_car_1 = session.query(Car).get(1)
db_car_2 = session.query(Car).get(2)

print(db_car_1.model)  # prints 'X5'
print(db_car_2.model)  # prints 'Camry'


# Update
db_car_2.model = 'Tesla'

session.add(db_car_2)
session.commit()

db_car_2 = session.query(Car).get(2)

print(db_car_2.model)  # prints 'Tesla'


# Delete
session.delete(db_car_2)
session.commit()

db_car_2 = session.query(Car).get(2)

print(db_car_2)  # prints 'None'
