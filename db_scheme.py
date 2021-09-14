#!/usr/bin/python3
from sqlalchemy.dialects.mysql import BOOLEAN, DATETIME, INTEGER, SET, SMALLINT, TEXT, TIME, TIMESTAMP, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Date, Integer, String, Table, ForeignKey 
from sqlalchemy.orm import relationship 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('mysql://dmarc:dmarc1234@localhost/dmarc')
db_session = Session(engine, future=True)
# dialect+driver://username:password@host:port/database

Base = declarative_base()

class Metadata(Base):
    __tablename__ = 'metadata'
    dmarc_id = Column(INTEGER, primary_key=True)
    org_name = Column(VARCHAR(25), nullable=False)
    report_id = Column(VARCHAR(25), nullable=False)
    date_begin = Column(DATETIME, nullable=False)
    date_end = Column(DATETIME, nullable=False)

class Policy(Base): 
    __tablename__ = 'policy'
    policy_id = Column(INTEGER, primary_key=True)
    dmarc_id = Column(Integer, ForeignKey('metadata.dmarc_id'))
    domain = Column(VARCHAR(255), nullable=False)
    adkim = Column(VARCHAR(1))
    aspf = Column(VARCHAR(1))
    policy = Column(VARCHAR(1))
    subpolicy = Column(VARCHAR(1), nullable=False)
    pct = Column(TINYINT, nullable=False)

class Record(Base): 
    __tablename__ = 'record'
    record_id = Column(INTEGER, primary_key=True)
    dmarc_id = Column(Integer, ForeignKey('metadata.dmarc_id'))

class Row(Base):
    __tablename__ = 'row'
    row_id = Column(INTEGER, primary_key=True)
    record_id = Column(Integer, ForeignKey('record.record_id'))
    source_ip = Column(VARCHAR(15), nullable=False)
    count = Column(INTEGER, nullable=False)
    disposition = Column(VARCHAR(1))
    dkim = Column(BOOLEAN)
    spf = Column(BOOLEAN)
    header_from = Column(VARCHAR(255))

class Auth_Result(Base): 
    __tablename__ = 'auth_result'
    auth_results_id = Column(INTEGER, primary_key=True)
    record_id = Column(Integer, ForeignKey('record.record_id'))
    dkim_domain = Column(VARCHAR(255))
    dkim_result = Column(BOOLEAN)
    spf_domain = Column(VARCHAR(255))
    spf_result = Column(BOOLEAN)

Base.metadata.create_all(engine)
