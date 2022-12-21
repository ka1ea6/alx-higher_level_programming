#!/usr/bin/python3
'''Script to list all State objects that contain the
letter a from the database hbtn_0e_6_usa'''


import sys
from relationship_state import Base, State
from relationship_city import City
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

        Base.metadata.create_all(engine)

        res = session.query(State, City)\
            .filter(City.state_id == State.id).all()
        res_dict = {f"{key}": [] for key, _ in res}
        for instance in res:
            res_dict[f"{instance[0]}"].append(instance[1])

        for state in res_dict:
            print(state)
            for city in res_dict[state]:
                print(f"\t{city}")
        # for state in session.query(State):
        #     print(state)
        #     for city in session.query(City).\
        #       filter(City.state_id == state.id):
        #         print(f"\t{city}")

    else:
        print(f"Usage: ./12-model_state_update_id_2.py \
        <mysql_username> <mysql_password> <database_name>")
