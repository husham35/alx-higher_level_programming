#!/usr/bin/python3
"""
A script that list all states from the `hbtn_0e_0_usa`
database  where name matches the argument
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
    SELECT *
    FROM states
    WHERE BINARY name = '{}'
    ORDER BY id
    """.format(arg)

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
