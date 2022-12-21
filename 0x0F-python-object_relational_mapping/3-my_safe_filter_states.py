#!/usr/bin/python3
"""
Filter states by user input safe from MySQL injections!
It takes in an argument and displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
     db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])
    
    db_rows = cursor.fetchall()
    for i in db_rows:
        print(i)
    
    cursor.close()
    db.close()
