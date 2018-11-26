'''
Created on 11-Nov-2018

@author: duttasudip89
'''
from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Date

class InventoryItems (Base):
    __tablename__ = "inventory_item_tbl"
    __table_args__ = {'schema' : 'apps'}
    item_id = Column('item_id', Integer, Sequence('item_id_sequence', schema='apps') , primary_key = True)
    item_number = Column('item_number', String)
    organization_id = Column('organization_id', Integer)
    enabled_flag = Column('enabled_flag', String)
    description = Column('description', String)
    buyer_id = Column('buyer_id', Integer)
    item_type = Column('item_type', String)
    long_description = Column('long_description', String)
    asset_flag = Column('asset_flag', String)
    asset_id = Column('asset_id', Integer)
    purchasing_enabled_flag = Column('purchasing_enabled_flag', String)
    customer_order_enabled_flag = Column('customer_order_enabled_flag', String)
    returnable_flag = Column('returnable_flag', String)
    inspection_required_flag = Column('inspection_required_flag', String)
    list_price_per_unit = Column('list_price_per_unit', String)
    shelf_life_days = Column('shelf_life_days', String)
    item_control_code = Column('item_control_code', String)
    min_order_quantity = Column('min_order_quantity', String)
    max_order_quantity = Column('max_order_quantity', String)
    planner_code = Column('planner_code', String)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    creation_date = Column('creation_date', DateTime)
    created_by = Column('created_by', Integer)