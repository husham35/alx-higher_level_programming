#!/usr/bin/python3
"""
A script that lists all states from the
`hbtn_0e_0_usa` database with a name starting with `N`
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306
    statement: str = """
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

    cursor.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
