from sqlalchemy import create_engine
from .schema import metadata_obj
from sqlalchemy.orm import sessionmaker

def do():
    engine = create_engine('sqlite:///movies.db', echo=True)
    metadata_obj.create_all(engine)
    session = sessionmaker(bind=engine)
