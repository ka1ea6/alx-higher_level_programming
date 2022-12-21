#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,primary_key=True, nullable=False, unique=True)
    name = Column(String(length=128))
