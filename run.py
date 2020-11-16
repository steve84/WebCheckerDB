from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import time
import uuid

from models import metadata, Job, Version

db_file = 'webtracker.db'
conn_string = 'sqlite:///%s' % db_file
engine = create_engine(conn_string)
Session = sessionmaker(bind=engine)
session = Session()

metadata.create_all(engine)

actual_time = int(time.time()*1000)

job = Job(
    dir=-1,
    ordinal=1,
    name='Lego.com Sale',
    freq_mobile=-1,
    lastresult=0,
    knownVersion=None,
    address='https://www.lego.com/de-ch/categories/sales-and-deals',
    css='#blteb53aaee7208a978 section div div div.Productsstyles__ProductsWrapper-r9qrnh-0.erhzcf ul li:nth-child(1) div div.ProductLeafSharedstyles__Column-sc-1epu2xb-1.eTTqVI div.ProductLeafSharedstyles__DetailsRow-sc-1epu2xb-4.uVRhD a h2 span',
    ua='Mozilla/5.0 (Linux; Android 7.1.2; ASUS_Z01QD Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36',
    lm=actual_time,
    guid=bytes.fromhex(uuid.uuid4().hex),
    flags=24784
)

session.add(job)
session.commit()

# version = Version(
#     jobid=job._id,
#     time=actual_time,
#     data=bytes(bytearray.fromhex('31').decode(), 'utf8'),
#     flags=0
# )

# session.add(version)
# session.commit()

# job.knownVersion = version._id
# session.commit()

session.close()
