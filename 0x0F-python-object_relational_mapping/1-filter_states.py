#!/usr/bin/python3
"""
A script that lists all states from the
`hbtn_0e_0_usa` database with a name starting with `N`
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
    SELECT *
    FROM states
    WHERE BINARY name LIKE 'N%'
    ORDER BY id
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
    filtered_rows = cursor.fetchall()
    for row in filtered_rows:
        print(row)
