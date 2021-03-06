'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base, PurchaseTrxHeader
from sqlalchemy.sql.schema import Column, Sequence,ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
import datetime

class PurchaseTrxLines (Base):
    __tablename__ = "purchase_trx_lines_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_line_id = Column('transaction_line_id', Integer, Sequence('purchase_trx_lines_sequence', schema='apps') , primary_key = True)
    transaction_header_id = Column('transaction_header_id', Integer,ForeignKey('apps.purchase_trx_header_tbl.transaction_header_id'))
    item_id = Column('item_id', Integer)
    booking_unit_price = Column('booking_unit_price', Float)
    booking_quantity = Column('booking_quantity', Float)
    unit_of_measure = Column('unit_of_measure', String)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    line_number = Column('line_number', Integer ,nullable=False)
    
    purchase_trx_header = relationship("model.PurchaseTrxHeader.PurchaseTrxHeader", back_populates="purchase_trx_lines")