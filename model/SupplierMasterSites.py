'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base, SupplierMasterHeader
from sqlalchemy.sql.schema import Column, Sequence,ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Date
from sqlalchemy.orm import relationship
import datetime

class SupplierMasterSites (Base):
    __tablename__ = "supplier_master_sites_tbl"
    __table_args__ = {'schema' : 'apps'}
    supplier_site_id = Column('supplier_site_id', Integer, Sequence('supplier_site_id_sequence', schema='apps') , primary_key = True)
    supplier_id = Column('supplier_id', Integer,ForeignKey('apps.supplier_master_header_tbl.supplier_id'))
    supplier_site_code = Column('supplier_site_code', String)
    supplier_site_address = Column('supplier_site_address', String)
    phone_number1 = Column('phone_number1', String)
    phone_number2 = Column('phone_number2', String)
    email = Column('email', String)
    payment_method_lookup_code = Column('payment_method_lookup_code', String)
    gstin_number = Column('gstin_number', String)
    pay_group_lookup_code = Column('pay_group_lookup_code', String)
    payment_term = Column('payment_term', String)
    purchasing_site_flag = Column('purchasing_site_flag', String)
    rfq_only_site = Column('rfq_only_site', String)
    tax_registration_number = Column('tax_registration_number', String)
    inactive_date = Column('inactive_date', Date)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime,default=datetime.datetime.utcnow)
    last_update_date = Column('last_update_date',DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_updated_by = Column('last_updated_by', Integer)
    
    supplier = relationship("model.SupplierMasterHeader.SupplierMasterHeader", back_populates="sites")
    
        