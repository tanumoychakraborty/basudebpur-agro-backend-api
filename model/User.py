'''
Created on 27-Oct-2018

@author: tanumoy
'''
from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from sqlalchemy.orm import relationship


class User (Base):
    __tablename__ = "user_tbl"
    __table_args__ = {'schema' : 'apps'}
    user_id = Column('user_id', Integer, Sequence('user_id_sequence', schema='apps') , primary_key = True)
    user_name = Column('user_name', String)
    description = Column('description', String)
    Phone_number1 = Column('phone_number1', String)
    Phone_number2 = Column('phone_number2', String)
    email = Column('email', String)
    password = Column('password', String)
    user_type = Column('user_type', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    created_by = Column('created_by', Integer)
    creation_date = Column('creation_date', DateTime)
    last_update_date = Column('last_update_date', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    password_life_span = Column('password_life_span', Integer)
    employee_id = Column('employee_id', Integer)
