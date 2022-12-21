#!/usr/bin/python3
"""
Module that Lists all State objects, and 
corresponding City objects through Alchemy from the database
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for a_city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(a_city.id, a_city.name,
                  a_city.state.name))
    session.close()
