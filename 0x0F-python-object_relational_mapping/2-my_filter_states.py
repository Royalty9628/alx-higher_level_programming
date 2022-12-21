#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    db_query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cursor.execute(db_query)

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()
