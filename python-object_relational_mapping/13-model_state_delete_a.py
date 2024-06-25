#!/usr/bin/python3
"""ORM pa buena"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


def listState(user, passw, dbName):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, dbName), pool_pre_ping=True)

    session = Session(engine)

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    session.commit()

    session.close()


if __name__ == '__main__':
    us = argv[1]
    pas = argv[2]
    db = argv[3]

    listState(us, pas, db)
