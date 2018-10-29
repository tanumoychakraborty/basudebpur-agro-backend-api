'''
Created on 27-Oct-2018

@author: tanumoy
'''
from model import Base
from sqlalchemy.sql.schema import Column, Sequence
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Date

class Person (Base):
    __tablename__ = "Person_tbl"
    person_id = Column('Person_id', Integer, Sequence('person_id_sequence') , primary_key = True)
    middle_name = Column('Middle_Name', String)
    last_name = Column('Last_Name', String)
    date_of_birth = Column('date_of_birth', Date)
    gender = Column('Gender', String)
    address = Column('Address', String)
    phone_number1 = Column('Phone_number1', String)
    phone_number2 = Column('Phone_number2', String)
    email = Column('email', String)
    effective_from = Column('effective_from', DateTime)
    effective_to = Column('effective_to', DateTime)
    #user_tbl_user_id = Column('User_tbl_user_id', Integer)

    