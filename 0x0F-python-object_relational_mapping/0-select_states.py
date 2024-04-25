#!/usr/bin/python3
"""
A script that lists all states from the database `hbtn_0e_0_usa`
"""

import sys
# import pymysql
# pymysql.install_as_MySQLdb()
# import mysql.connector as MySQLdb
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    query = """SELECT * FROM states ORDER BY id"""

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(query)
    states_rows = cursor.fetchall()
    for state_row in states_rows:
        print(state_row)
