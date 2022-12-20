#!/usr/bin/python3
'''Python script for connecting to a database and executing a
fetch query'''
import sys
import MySQLdb

if len(sys.argv) > 3:
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="127.0.0.1",
                         user=user_name,
                         passwd=passwd,
                         db=db_name)
    cur = db.cursor()
    cur.execute('SELECT * FROM states;')
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
else:
    print(f"Usage: ./0-select_states.py \
    <mysql_username> <mysql_password> <database_name>")
