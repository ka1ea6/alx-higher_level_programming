#!/usr/bin/python3
'''Script to list all State objects that contain the
letter a from the database hbtn_0e_6_usa'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) > 4:
        user_name = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        engine = create_engine(f"mysql+mysqldb:\
//{user_name}:{passwd}@localhost:3306/{db_name}")

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).order_by(State.id)\
                                    .filter(State.name == state_name).first()

        print("Not found" if not state else state.id)
    else:
        print(f"Usage: ./10-model_state_my_get.py \
        <mysql_username> <mysql_password> <database_name>")
