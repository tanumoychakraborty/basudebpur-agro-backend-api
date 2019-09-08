'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, LargeBinary,\
    Float
import datetime
from sqlalchemy.orm import relationship


class SalesTrxHeader (Base):
    __tablename__ = "sales_trx_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_header_id = Column('transaction_header_id', Integer, Sequence('sales_trx_header_sequence', schema='apps') , primary_key = True)
    sales_trx_number = Column('sales_trx_number', String)
    transaction_date = Column('transaction_date', DateTime,default=datetime.datetime.utcnow)
    order_status = Column('order_status', String)
    customer_id = Column('customer_id', Integer)
    sales_rep_id = Column('sales_rep_id', Integer)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    
    sales_trx_lines = relationship('model.SalesTrxLines.SalesTrxLines', back_populates='sales_trx_header')