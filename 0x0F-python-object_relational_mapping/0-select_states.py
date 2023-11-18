#!/usr/bin/python3
""" lists all states in the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    Cursor = db.cursor()
    Cursor.execute("SELECT * FROM states")

    rows = Cursor.fetchall()
    for i in rows:
        print(i)
    Cursor.close()
    db.close()
