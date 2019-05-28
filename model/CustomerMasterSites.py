'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base
from sqlalchemy.sql.schema import Column, Sequence,ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from sqlalchemy.orm import relationship
import datetime


class CustomerMasterSites (Base):
    __tablename__ = "customer_master_sites_tbl"
    __table_args__ = {'schema' : 'apps'}
    customer_site_id = Column('customer_site_id', Integer, Sequence('customer_site_id_sequence', schema='apps') , primary_key = True)
    customer_id = Column('customer_id', Integer,ForeignKey('apps.customer_master_header_tbl.customer_id'))
    customer_site_code = Column('customer_site_code', String)
    customer_address = Column('customer_address', String)
    phone_number1 = Column('phone_number1', String)
    phone_number2 = Column('phone_number2', String)
    email = Column('email', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date',DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    
    customer = relationship("model.CustomerMasterHeader.CustomerMasterHeader", back_populates="sites")