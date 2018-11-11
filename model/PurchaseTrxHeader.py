'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, LargeBinary

class PurchaseTrxHeader (Base):
    __tablename__ = "purchase_trx_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_header_id = Column('transaction_header_id', Integer, Sequence('apps.purchase_trx_header_sequence') , primary_key = True)
    purchase_trx_number = Column('purchase_trx_number', String)
    transaction_date = Column('transaction_date', DateTime)
    order_type = Column('order_type', String)
    order_status = Column('Order_status', String)
    buyer_id = Column('buyer_id', Integer)
    suppplier_id = Column('suppplier_id', Integer)
    amount = Column('amount', Integer)
    weighting_number = Column('weighting_Number', String)
    ref_doc = Column('ref_doc', LargeBinary)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    
    
        