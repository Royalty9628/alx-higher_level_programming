#!/usr/bin/python3
"""
Lists all cities from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()

    db_cursor.execute("SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states\
             WHERE cities.state_id = states.id")

     rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(rows_selected)

    db_cursor.close()
    db.close()
