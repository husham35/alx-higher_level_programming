#!/usr/bin/python3
"""
A script that lists all `State` objects that contain
the letter `a` from the database `hbtn_0e_6_usa`
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    Session = sessionmaker()
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@{host}/{db_name}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    if (
        query := session.query(State)
        .order_by(State.id)
        .filter(State.name.contains("a"))
    ):
        for state in query:
            print(state.id, state.name, sep=": ")
