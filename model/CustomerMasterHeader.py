'''
Created on 11-Nov-2018

@author: duttasudip89
'''

from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Date


class CustomerMasterHeader (Base):
    __tablename__ = "customer_master_header_tbl"
    __table_args__ = {'schema' : 'apps'}
    customer_id = Column('customer_id', Integer, Sequence('apps.customer_id_sequence') , primary_key = True)
    customer_code = Column('customer_code', String)
    customer_name = Column('customer_name', String)
    description = Column('description', String)
    customer_type = Column('customer_type', String)
    remarks = Column('remarks', String)
    enabled_flag = Column('enabled_flag', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    created_by = Column('created_by', int)  
    creation_date = Column('effective_from', DateTime)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', int)