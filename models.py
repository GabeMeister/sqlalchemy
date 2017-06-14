# pylint: disable=C0111,C0103

from sqlalchemy import Column, ForeignKey, Integer, String, BLOB, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    is_admin = Column(Boolean, nullable=False)

    def __str__(self):
        return self.name
