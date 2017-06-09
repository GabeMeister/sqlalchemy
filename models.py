# pylint: disable=C0111,C0103

from sqlalchemy import Column, ForeignKey, Integer, String, BLOB, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    old_age = Column(Integer)

    def __str__(self):
        return self.name


# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     street_number = Column(String(250))
#     street_name = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def __str__(self):
#         return '{0} {1} {2}'.format(self.street_number, self.street_name, self.post_code)


# class SampleData(Base):
#     __tablename__ = 'sample'
#     id = Column(Integer, primary_key=True)
#     text = Column(BLOB)
#     sample_date = Column(DateTime)
