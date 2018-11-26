'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base, PurchaseTrxHeader
from sqlalchemy.sql.schema import Column, Sequence,ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from sqlalchemy.orm import relationship

class PurchaseTrxLines (Base):
    __tablename__ = "purchase_trx_lines_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_line_id = Column('transaction_line_id', Integer, Sequence('purchase_trx_lines_sequence', schema='apps') , primary_key = True)
    transaction_header_id = Column('transaction_header_id', Integer,ForeignKey('apps.purchase_trx_header_tbl.transaction_header_id'))
    item_id = Column('item_id', Integer)
    item_description = Column('item_description', String)
    unit_price = Column('unit_price', Integer)
    quantity = Column('quantity', Integer)
    receipt_unit_price = Column('receipt_unit_price', Integer)
    receipt_qty = Column('receipt_qty', Integer)
    unit_of_measure = Column('unit_of_measure', String)
    line_status = Column('line_status', String)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    
    purchase_trx_header = relationship("model.PurchaseTrxHeader.PurchaseTrxHeader", back_populates="purchase_trx_lines")
        