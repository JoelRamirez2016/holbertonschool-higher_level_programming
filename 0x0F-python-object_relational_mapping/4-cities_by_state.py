#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities INNER JOIN states ON cities.state_id = states.id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
