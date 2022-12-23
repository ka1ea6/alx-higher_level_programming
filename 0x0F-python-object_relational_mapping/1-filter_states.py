#!/usr/bin/python3
'''Python script to list all states with a
name starting with N from the db hbtn_0e_0_usa'''

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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%';")
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
else:
    print(f"Usage: ./1-filter_states.py \
    <mysql_username> <mysql_password> <database_name>")
