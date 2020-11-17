from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import csv
import time
import uuid

from models import metadata, Job, Version

db_file = 'webtracker.db'
conn_string = 'sqlite:///%s' % db_file
engine = create_engine(conn_string)
Session = sessionmaker(bind=engine)
session = Session()

metadata.create_all(engine)


with open('jobs.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    i = 1
    for row in reader:
        actual_time = int(time.time()*1000)

        job = Job(
            dir=-1,
            ordinal=i,
            name=row['name'],
            freq_mobile=-1,
            freq_wifi=int(row['frequency']),
            lastresult=0,
            knownVersion=None,
            address=row['url'],
            css=row['css'].replace(' > ', ' '),
            ua=(
                'Mozilla/5.0 (Linux; Android 7.1.2; '
                'ASUS_Z01QD Build/N2G48H; wv) AppleWebKit/537.36'
                ' (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158'
                ' Mobile Safari/537.36'
                ),
            lm=actual_time,
            guid=bytes.fromhex(uuid.uuid4().hex),
            flags=24784
        )

        session.add(job)
        session.commit()

session.close()
