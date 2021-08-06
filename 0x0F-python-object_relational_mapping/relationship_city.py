#!/usr/bin/python3

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")
