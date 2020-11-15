from sqlalchemy import create_engine

from models import metadata

db_file = 'test.db'
conn_string = 'sqlite:///%s' % db_file
engine = create_engine(conn_string)

metadata.create_all(engine)