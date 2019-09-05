'''
Created on 19-Jun-2019

@author: duttasudip89
'''

from model import Base, ReceiptHeader
from sqlalchemy.sql.schema import Column, Sequence, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, LargeBinary,\
    Float
import datetime
from sqlalchemy.orm import relationship

class ReceiptHeader (Base):
    __tablename__ = "receipt_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    receipt_header_id = Column('receipt_header_id', Integer, Sequence('receipt_header_sequence', schema='apps') , primary_key = True)
    receipt_number = Column('receipt_number', String)
    challan_number = Column('challan_number', String)
    receipt_date = Column('receipt_date', DateTime)
    challan_date = Column('challan_date', DateTime)
    source_transaction_header_id = Column('source_transaction_header_id', String)
    source_transaction_type = Column('source_transaction_type',String)
    vehicle_number = Column('vehicle_number', String)
    bata = Column('bata',Float)
    net_weight = Column('net_weight',Float)
    average_weight = Column('average_weight',Float)
    total_bags = Column('total_bags',Float)
    unit_of_measure =Column('unit_of_measure',String, default='KG')
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    receipt_header_status = Column('receipt_header_status', String)
    
    receipt_lines = relationship('model.ReceiptLines.ReceiptLines', back_populates='receipt_header')