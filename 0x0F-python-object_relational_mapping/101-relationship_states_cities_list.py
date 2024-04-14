#!/usr/bin/python3
"""
A script that lists all `State` objects, and corresponding
`City` objects, contained in the database `hbtn_0e_101_usa`
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    Session = sessionmaker()
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@{host}:{port}/{db_name}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    if states := session.query(State).order_by(State.id):
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    session.close()
