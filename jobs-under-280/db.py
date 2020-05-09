from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def initialize_db(db_uri):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    return Session()