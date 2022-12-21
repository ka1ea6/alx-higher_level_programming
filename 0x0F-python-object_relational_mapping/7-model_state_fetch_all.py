#!/usr/bin/python3
'''Script that lists all state objects form the
database hbtn_0e_6_usa'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker


if len(sys.argv) > 3:
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb:\
//{user_name}:{passwd}@localhost:3306/{db_name}")

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(instance)

else:
    print(f"Usage: ./7-model_state_fetch_all.py \
    <mysql_username> <mysql_password> <database_name>")
