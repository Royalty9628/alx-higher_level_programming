#!/usr/bin/python3
"""
Filter states by user input safe from MySQL injections!
It takes in an argument and displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name = %s", [argv[4]])


    for state in cursor.fetchall():
        print(state)
    db_cursor.close()
    db.close()