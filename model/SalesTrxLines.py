'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base
from sqlalchemy.sql.schema import Column, Sequence,ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from sqlalchemy.orm import relationship

class SalesTrxLines (Base):
    __tablename__ = "sales_trx_lines_tbl"
    __table_args__ = {'schema' : 'apps'}
    transaction_line_id = Column('transaction_line_id', Integer, Sequence('purchase_trx_lines_sequence', schema='apps') , primary_key = True)
    transaction_header_id = Column('transaction_header_id', Integer,ForeignKey('sales_trx_header_tbl.transaction_header_id'))    
    item_id = Column('item_id', Integer)
    item_description = Column('item_description', String)
    unit_price = Column('unit_price', Integer)
    quantity = Column('quantity', Integer)
    unit_of_measure = Column('unit_of_measure', String)
    line_status = Column('line_status', String)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    
    purchase_trx_header = relationship("model.SalesTrxHeader", back_populates="sales_trx_lines")