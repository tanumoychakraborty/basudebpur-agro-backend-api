'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base, SupplierMasterSites
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Date
from sqlalchemy.orm import relationship
import datetime

class SupplierMasterHeader (Base):
    __tablename__ = "supplier_master_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    supplier_id = Column('supplier_id', Integer, Sequence('supplier_id_sequence', schema='apps') , primary_key = True)
    supplier_code = Column('supplier_code', String)
    supplier_name = Column('supplier_name', String)
    description = Column('description', String)
    supplier_type = Column('supplier_type', String)
    remarks = Column('remarks', String)
    enabled_flag = Column('enabled_flag', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    employee_id = Column('employee_id', Integer)
    ship_to_location_code = Column('ship_to_location_code', String)
    bill_to_location_code = Column('bill_to_location_code', String)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date',DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    
    sites = relationship('model.SupplierMasterSites.SupplierMasterSites', back_populates='supplier')