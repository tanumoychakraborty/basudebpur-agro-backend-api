'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base, PurchaseTrxLines
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, LargeBinary
import datetime
from sqlalchemy.orm import relationship

class PurchaseTrxHeader (Base):
    __tablename__ = "purchase_trx_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_header_id = Column('transaction_header_id', Integer, Sequence('purchase_trx_header_sequence', schema='apps') , primary_key = True)
    purchase_trx_number = Column('purchase_trx_number', String)
    transaction_date = Column('transaction_date', DateTime,default=datetime.datetime.utcnow)
    order_type = Column('order_type', String)
    order_status = Column('order_status', String)
    buyer_id = Column('buyer_id', Integer)
    suppplier_id = Column('suppplier_id', Integer)
    amount = Column('amount', Integer)
    weighting_number = Column('weighting_number', String)
    ref_doc = Column('ref_doc', LargeBinary)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    vehicle_number  = Column('vehicle_number', String)
    
    purchase_trx_lines = relationship('model.PurchaseTrxLines.PurchaseTrxLines', back_populates='purchase_trx_header')