'''
Created on 21-Dec-2018

@author: duttasudip89
'''


from model import Base
from sqlalchemy.sql.schema import Column,Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
import datetime

class CommonLookups (Base):
    __tablename__ = "common_lookup_tbl"
    __table_args__ = {'schema' : 'apps'}
    primary_id = Column('primary_id', Integer, Sequence('lookup_primary_id_sequence', schema='apps') , primary_key = True)
    lookup_name = Column('lookup_name', String)
    lookup_code = Column('lookup_code', String)
    meaning = Column('meaning', String)
    description = Column('description', String)
    tag = Column('tag', String)
    enabled = Column('enabled', String)
    effective_from = Column('effective_from', DateTime,default=datetime.datetime.utcnow)
    effective_to = Column('effective_to', DateTime)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)