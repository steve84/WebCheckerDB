# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, LargeBinary, Table, Text, text, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Filter(Base):
    __tablename__ = 'Filters'

    job = Column(ForeignKey('Jobs._id', ondelete='CASCADE'), primary_key=True, nullable=False)
    ordinal = Column(Integer, primary_key=True, nullable=False)
    type = Column(Integer, nullable=False)
    pattern = Column(Text, nullable=False)
    flags = Column(Integer, nullable=False, server_default=text("0"))

    Job = relationship('Job')


class Job(Base):
    __tablename__ = 'Jobs'
    __table_args__ = {'sqlite_autoincrement': True}

    _id = Column(Integer, primary_key=True)
    dir = Column(Integer, server_default=text("NULL"))
    ordinal = Column(Integer, nullable=False)
    name = Column(Text)
    freq_mobile = Column(Integer, nullable=False)
    freq_wifi = Column(Integer, nullable=False, server_default=text("-1"))
    lastcheck = Column(Integer, nullable=False, server_default=text("-1"))
    lastcheckerror = Column(Integer, nullable=False, server_default=text("-1"))
    lastresult = Column(Integer, nullable=False)
    lastresultrepeated = Column(Integer, nullable=False, server_default=text("0"))
    changes = Column(Integer, nullable=False, server_default=text("0"))
    knownVersion = Column(ForeignKey('Versions._id', ondelete='SET NULL'))
    address = Column(Text)
    css = Column(Text)
    ua = Column(Text, server_default=text("NULL"))
    al = Column(Text, server_default=text("NULL"))
    whitelist = Column(Text, server_default=text("NULL"))
    blacklist = Column(Text, server_default=text("NULL"))
    numbermatch = Column(Text, server_default=text("NULL"))
    minchange = Column(Float, server_default=text("NULL"))
    tstart = Column(Integer, server_default=text("-1"))
    tend = Column(Integer, server_default=text("-1"))
    tdays = Column(Integer, server_default=text("0"))
    lm = Column(Integer, nullable=False)
    guid = Column(BLOB, nullable=False)
    flags = Column(Integer, nullable=False, server_default=text("0"))
    deleted = Column(Integer, server_default=text("NULL"))
    extra = Column(Text, server_default=text("NULL"))
    let = Column(Integer)
    lmet = Column(Integer)
    lst = Column(Integer)
    lvt = Column(Integer)
    timeCreated = Column(Integer, server_default=text("NULL"))


    Version = relationship('Version', primaryjoin='Job.knownVersion == Version._id')


class Log(Base):
    __tablename__ = 'Log'

    job = Column(ForeignKey('Jobs._id', ondelete='CASCADE'), primary_key=True, nullable=False)
    batch = Column(Integer, primary_key=True, nullable=False)
    entry = Column(Integer, primary_key=True, nullable=False)
    time = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False, server_default=text("800"))
    msg = Column(Text, nullable=False)
    param1 = Column(Text, server_default=text("NULL"))
    param2 = Column(Text, server_default=text("NULL"))
    param3 = Column(Text, server_default=text("NULL"))

    Job = relationship('Job')


class Macro(Base):
    __tablename__ = 'Macros'

    job = Column(ForeignKey('Jobs._id', ondelete='CASCADE'), primary_key=True, nullable=False)
    step = Column(Integer, primary_key=True, nullable=False)
    name = Column(Integer, nullable=False)
    origin = Column(Text, server_default=text("NULL"))
    css = Column(Text, server_default=text("NULL"))
    target = Column(Text, nullable=False)
    content = Column(BLOB, server_default=text("NULL"))
    flags = Column(Integer, nullable=False, server_default=text("0"))

    Job = relationship('Job')


class Version(Base):
    __tablename__ = 'Versions'
    __table_args__ = {'sqlite_autoincrement': True}

    _id = Column(Integer, primary_key=True)
    jobid = Column(ForeignKey('Jobs._id', ondelete='CASCADE'), nullable=False)
    time = Column(Integer, nullable=False)
    data = Column(BLOB, nullable=False)
    flags = Column(Integer, nullable=False, server_default=text("0"))
    url = Column(Text, server_default=text("NULL"))
    log = Column(Integer, server_default=text("NULL"))

    Job = relationship('Job', primaryjoin='Version.jobid == Job._id')


t_android_metadata = Table(
    'android_metadata', metadata,
    Column('locale', Text)
)

