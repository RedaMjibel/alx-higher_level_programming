#!/usr/bin/python3

"""
lists State name and city objects from the database
hbtn_0e_6_usa with statename
"""

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    Base.metadata.create_all(engine)

    mycity = session.query(State, City).join(City).order_by(City.id)
    for states, cities in mycity:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

    session.close()
