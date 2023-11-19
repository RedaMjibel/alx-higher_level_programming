#!/usr/bin/python3
""" lists all cities in the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    Cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    Cursor.execute(query)

    rows = Cursor.fetchall()
    for i in rows:
        print(i)
    Cursor.close()
    db.close()
