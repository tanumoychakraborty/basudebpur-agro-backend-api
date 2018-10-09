'''
Created on 03-Oct-2018

@author: tanumoy
'''
from model import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

class test(Base):
    '''
    test class for db connection checking
    '''

    __tablename__ = 'test'
    
    test = Column(String, primary_key=True)
