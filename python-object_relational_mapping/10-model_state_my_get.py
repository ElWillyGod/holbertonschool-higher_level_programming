#!/usr/bin/python3
"""ORM pa buena"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


def listState(user, passw, dbName, name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, dbName), pool_pre_ping=True)

    session = Session(engine)

    state = session.query(State).filter(State.name == name).first()

    if state:
        print("{}".format(state.id))
    else:
        print('Not found')

    session.close()


if __name__ == '__main__':
    us = argv[1]
    pas = argv[2]
    db = argv[3]
    name = argv[4]

    listState(us, pas, db, name)
