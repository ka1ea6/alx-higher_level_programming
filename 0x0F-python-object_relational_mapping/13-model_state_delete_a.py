#!/usr/bin/python3
'''Script to list all State objects that contain the
letter a from the database hbtn_0e_6_usa'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) > 3:
        user_name = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]

        engine = create_engine(f"mysql+mysqldb:\
//{user_name}:{passwd}@localhost:3306/{db_name}")

        Session = sessionmaker(bind=engine)
        session = Session()

        to_del = session.query(State).filter(State.name.like("%a%"))

        for instance in to_del:
            session.delete(instance)
        session.commit()
    else:
        print(f"Usage: ./12-model_state_update_id_2.py \
        <mysql_username> <mysql_password> <database_name>")
