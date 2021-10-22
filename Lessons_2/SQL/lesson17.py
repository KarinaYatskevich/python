from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///lesson17.db")
base = declarative_base()
session = sessionmaker(bind=engine)()


class Group(base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)



class Student(base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group_id = Column(Integer, ForeignKey('group.id', ondelete='set null'), nullable=True)


base.metadata.drop_all(engine)  # drop all tables
base.metadata.create_all(engine)  # create all tables

g1 = Group(name = 106)
g2 = Group(name = 107)

session.add_all([g1, g2 ])
session.commit()

s1 = Student(first_name = 'Karina', last_name = 'Yatskevich', group_id = g1.id)
s2 = Student(first_name = 'marina', last_name = 'Yatskevich', group_id = g2.id)

session.add_all([s1, s2])
session.commit()



results = session.query(Student, Group).join(Group, Student.group_id == Group.id).all()
for res in results:
    print(f'id:{res.Student.id}, name: {res.Student.last_name}, group: {res.Group.name}')