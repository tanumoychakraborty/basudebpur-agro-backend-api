'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base, ReceiptLines
from sqlalchemy.sql.schema import Column, Sequence,ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
import datetime

class ReceiptLines (Base):
    __tablename__ = "receipt_lines_tbl"
    __table_args__ = {'schema' : 'apps'}
    receipt_line_id = Column('receipt_line_id', Integer, Sequence('receipt_lines_sequence', schema='apps') , primary_key = True)
    receipt_header_id = Column('receipt_header_id', Integer,ForeignKey('apps.receipt_header_tbl.receipt_header_id'))
    line_number = Column('line_number', Integer ,nullable=False)
    item_id = Column('item_id', Integer)
    load_unload_number =Column('load_unload_number',String)
    load_unload_area = Column('load_unload_area', String)
    weighing_number = Column('weighing_number', String)
    receipt_line_status =Column('receipt_line_status',String)
    quantity =Column('quantity',Float)
    unit_price=Column('unit_price',Float)
    unit_of_measure =Column('unit_of_measure',String)
    discount =Column('discount',Float)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    
    
    receipt_header = relationship("model.ReceiptHeader.ReceiptHeader", back_populates="receipt_lines")