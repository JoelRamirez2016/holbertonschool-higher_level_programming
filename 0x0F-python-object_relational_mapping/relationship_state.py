#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base();
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    definition of a State Class

    Attrs:
        __tablename__: name of the table in DB
        id: primary key column of the table
        name: column name of the table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete")
