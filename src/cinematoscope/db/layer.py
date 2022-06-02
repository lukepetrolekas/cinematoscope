from sqlalchemy import create_engine
from .schema import *
from sqlalchemy.orm import sessionmaker
import os
import csv

def do():
    engine = create_engine('sqlite:///movies.db', echo=True)
    metadata_obj.create_all(engine)
    SessionFactory = sessionmaker(bind=engine)

    with SessionFactory() as session:

        with open('src/cinematoscope/db/job.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

            next(spamreader, None)

            for row in spamreader:
                print(row)
                print(row[0])
                session.add(Job(name=row[0],wiki_pid=row[1]))

        session.commit()
    #session.close()