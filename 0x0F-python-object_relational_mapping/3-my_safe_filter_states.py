#!/usr/bin/python3
'''script that takes an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument'''

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
    query = "SELECT * FROM states WHERE name = %s;"
    cur.execute(query, (state_name,))
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
else:
    print(f"Usage: ./2-my_safe_filter_states.py \
    <mysql_username> <mysql_password> <database_name> <state_name>")
