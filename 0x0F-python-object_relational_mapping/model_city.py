#!/usr/bin/python3
"""
contains the class definition of a City
"""

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    definition of a City Class

    Attrs:
        __tablename__: name of the table in DB
        id: primary key column of the table
        name: column name of the table
        state_id: Foreign Key from the table states
        state: reference to the State instance
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")
