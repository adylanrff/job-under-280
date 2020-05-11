from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def initialize_db(db_uri, bases):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    for base in bases:
        base.metadata.create_all(engine)

    return Session()