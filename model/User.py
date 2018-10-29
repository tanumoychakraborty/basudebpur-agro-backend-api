'''
Created on 27-Oct-2018

@author: tanumoy
'''
from model import Base
from sqlalchemy.sql.schema import Column, ForeignKey, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from sqlalchemy.orm import relationship

class User (Base):
    __tablename__ = "User_tbl"
    user_id = Column('user_id', Integer, Sequence('user_id_sequence') , primary_key = True)
    user_name = Column('user_name', String)
    description = Column('description', String)
    Phone_number1 = Column('Phone_number1', String)
    Phone_number2 = Column('Phone_number2', String)
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
    person_tbl_person_id = Column('Person_tbl_Person_id', Integer, ForeignKey('Person.Person_id'))
    access_rights_tbl_access_id = Column('access_rights_tbl_access_id', Integer, ForeignKey('AccessRights.access_id'))

    person = relationship('Person', foreign_keys=person_tbl_person_id)
    access_rights = relationship('AccessRights', foreign_keys=access_rights_tbl_access_id)