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
        
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()


        res = session.query(State).outerjoin(City)\
            .order_by(State.id, City.id).all()

        for state in res:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")
    else:
        print(f"Usage: ./12-model_state_update_id_2.py \
        <mysql_username> <mysql_password> <database_name>")
