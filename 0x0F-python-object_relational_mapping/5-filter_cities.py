#!/usr/bin/python3
""" lists all cities in the database hbtn_0e_0_usa where the name is argv[4]"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    Cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    search = (argv[4],)
    Cursor.execute(query, search)

    rows = Cursor.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
        print(", ".join(j))
    Cursor.close()
    db.close()
