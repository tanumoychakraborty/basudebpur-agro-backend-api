'''
Created on 27-Oct-2018

@author: tanumoy
'''
from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime

class AccessRights (Base):
    __tablename__ = "access_rights_tbl"
    access_id = Column('access_id', Integer, Sequence('access_id_sequence') , primary_key = True)
    user_type = Column('user_type', String)
    access_area = Column('access_area', String)
    view = Column('view', String)
    create = Column('create', String)
    update = Column('update', String)
    delete = Column('delete', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime)
    last_update_date = Column('last_update_date', Integer)
    last_updated_by = Column('last_updated_by', Integer)