#!/usr/bin/python3
"""
A script that prints all `City` objects from the database `hbtn_0e_14_usa`
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    Session = sessionmaker()
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@{host}/{db_name}',
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    if cities := session.query(City).order_by(City.id):
        for city in cities:
            print(f'{city.state.name}: ({city.id}) {city.name}')
