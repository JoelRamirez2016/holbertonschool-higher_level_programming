#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import MySQLdb
import sys
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for city in session.query(City).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
