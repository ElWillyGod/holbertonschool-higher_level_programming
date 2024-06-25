#!/usr/bin/python3
"""ORM pa buena"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State
from model_city import City


def listState(user, passw, dbName):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, dbName), pool_pre_ping=True)

    session = Session(engine)

    for city, state in (session.query(City, State)
                        .filter(City.state_id == State.id)
                        .order_by(City.id).all()):

        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    us = argv[1]
    pas = argv[2]
    db = argv[3]

    listState(us, pas, db)
