#!/usr/bin/python3
'''Python file containing a class definition of a state using the
sqlalchemy ORM.'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''Class for representing the state table using the
    sqlalchemy ORM'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True)
    name = Column(String(length=128))

    def __repr__(self):
        return f"{self.id}: {self.name}"


# State.cities = relationship('City', back_populates="state")
