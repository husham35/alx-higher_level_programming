#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists
all `cities` of that state, using the database `hbtn_0e_4_usa`
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    arg = sys.argv[4]
    host = "localhost"
    port = 3306
    query = """
    SELECT c.id, c.name, s.name
    FROM cities AS c
    JOIN states AS s
    ON c.state_id = s.id
    HAVING BINARY s.name = %s
    ORDER BY c.id;
    """

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(query, (arg,))
    cities_rows = cursor.fetchall()
    cities = tuple(row[1] for row in cities_rows)
    cities = ', '.join(cities)
    print(cities)
