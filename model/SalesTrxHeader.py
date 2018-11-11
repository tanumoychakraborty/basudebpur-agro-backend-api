'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, LargeBinary

class SalesTrxHeader (Base):
    __tablename__ = "sales_trx_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_header_id = Column('transaction_header_id', Integer, Sequence('apps.sales_trx_header_sequence') , primary_key = True)
    transaction_number = Column('transaction_number', String)
    transaction_date = Column('transaction_date', DateTime)
    order_type = Column('order_type', String)
    order_status = Column('order_status', String)
    customer_id = Column('customer_id', Integer)
    amount = Column('Amount', Integer)
    weighting_number = Column('weighting_Number', String)
    ref_doc = Column('ref_doc', LargeBinary)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    