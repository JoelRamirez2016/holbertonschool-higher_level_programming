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
    cur.execute("SELECT cities.name \
                 FROM cities INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name LIKE %s", (sys.argv[4],))

    print(", ".join([row[0] for row in cur.fetchall()]))

    cur.close()
    conn.close()
