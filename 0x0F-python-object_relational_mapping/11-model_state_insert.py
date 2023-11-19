#!/usr/bin/python3

"""
lists State id object from the database hbtn_0e_6_usa with statename
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    Base.metadata.create_all(engine)

    addstate = State(name="Louisiana")
    session.add(addstate)
    session.commit()

    mystate = session.query(State).filter(State.name == "Louisiana").first()
    if mystate:
        print("{}".format(mystate.id))
    else:
        print("Not found")
    session.close()
