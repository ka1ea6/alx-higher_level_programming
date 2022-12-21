#!/usr/bin/python3
'''Script to list all State objects that contain the
letter a from the database hbtn_0e_6_usa'''


import sys
from model_state import Base, State
from model_city import City
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

        res = session.query(City).join(State)\
            .filter(City.state_id == State.id).all()

        for instance in res:
            print(f"{instance.state.name}: ({instance.id}) {instance.name}")
    else:
        print(f"Usage: ./12-model_state_update_id_2.py \
        <mysql_username> <mysql_password> <database_name>")
