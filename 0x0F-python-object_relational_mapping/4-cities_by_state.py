#!/usr/bin/python3
'''Script to list all cities from the database
hbtn+_0e_4_usa'''

import sys
import MySQLdb

if len(sys.argv) > 3:
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=user_name,
                         passwd=passwd,
                         db=db_name)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
    FROM cities LEFT JOIN states ON cities.state_id = states.id \
     ORDER BY %s;"
    cur.execute(query, ("cities.id",))
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
else:
    print(f"Usage: ./1-filter_states.py \
    <mysql_username> <mysql_password> <database_name>")
