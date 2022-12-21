#!/usr/bin/python3
'''Python file containing a class definition of a city using the
sqlalchemy ORM.'''


from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''Class for representing the city table using the
    sqlalchemy ORM'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        return f"{self.id}: {self.name}"
