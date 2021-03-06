from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'sqlite:///lecture16.sqlite', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete="set null"), nullable=True)

    def __init__(self, first_name, last_name, group_id):
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    students = relationship('Student', foreign_keys='Student.group_id')

# group1 = Group('Group 1')
# group2 = Group('Group 2')
#
# session.add_all([group1, group2])
# session.commit()
#
# st1 = Student('Ilya', 'B', group1.id)
#
# st2 = Student('Vasia', 'B', group2.id)
#
# session.add(st1)
# session.add(st2)
# session.commit()

# group = session.query(Group).first()
# students = group.students
#
# print(students)
#
# results = session.query(Student, Group).join(Group, Student.group_id == Group.id).all()
# for res in results:
#     print(f'id: {res.Student.id}, name: {res.Student.first_name}, group: {res.Group.name}')


