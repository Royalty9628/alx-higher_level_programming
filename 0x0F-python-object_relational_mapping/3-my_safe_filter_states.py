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
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
    
    cursor.close()
    db.close()
