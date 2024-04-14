#!/usr/bin/python3
"""
A script that lists all `cities` from the database `hbtn_0e_4_usa`
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    query = """
    SELECT c.id, c.name, s.name
    FROM cities AS c
    JOIN states AS s
    ON c.state_id = s.id
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

    cursor.execute(query)
    cities_rows = cursor.fetchall()
    for row in cities_rows:
        print(row)
