#!/usr/bin/python3
'''Python file containing a class definition of a state using the
sqlalchemy ORM.'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    '''Class for representing the state table using the
    sqlalchemy ORM'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(length=128))
