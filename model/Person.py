'''
Created on 27-Oct-2018

@author: tanumoy
'''
from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Date
from sqlalchemy.orm import relationship

class Person (Base):
    __tablename__ = "person_tbl"
    __table_args__ = {'schema' : 'apps'}
    person_id = Column('person_id', Integer, Sequence('person_id_sequence', schema='apps') , primary_key = True)
    employee_number = Column('employee_number', String)
    first_name = Column('first_name', String)
    middle_name = Column('middle_name', String)
    last_name = Column('last_name', String)
    date_of_birth = Column('date_of_birth', Date)
    gender = Column('gender', String)
    address = Column('address', String)
    phone_number1 = Column('phone_number1', String)
    phone_number2 = Column('phone_number2', String)
    email = Column('email', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    created_by = Column('created_by', Integer)
    creation_date = Column('effective_from', DateTime)
    last_updated_by = Column('last_updated_by', Integer)
    last_update_date = Column('last_update_date', DateTime)
    
    #employee = relationship('model.User', back_populates='person')