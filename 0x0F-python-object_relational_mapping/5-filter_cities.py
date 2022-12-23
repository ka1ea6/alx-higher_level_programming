#!/usr/bin/python3
'''Script to list all cities from the database
hbtn+_0e_4_usa'''

import sys
import MySQLdb

if len(sys.argv) > 4:
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user_name,
                         passwd=passwd,
                         db=db_name)
    cur = db.cursor()
    query = "SELECT cities.name\
    FROM cities LEFT JOIN states ON cities.state_id = states.id \
     WHERE states.name = %s;"
    cur.execute(query, (state_name,))
    states = cur.fetchall()

    print(", ".join([state[0] for state in states]))

    cur.close()
    db.close()
else:
    print(f"Usage: ./5-filter_cities.py \
    <mysql_username> <mysql_password> <database_name> <state_name>")
