'''
Created on 03-Oct-2018

@author: tanumoy
'''

from sqlalchemy import create_engine


class dbEngine(object):
    '''
    singletone class to access db engine
    '''
    
    dbengine = None
    
    @staticmethod
    def get():
        if not dbEngine.dbengine:
            dbEngine.dbengine = create_engine('postgresql://basudebpuragrodb:password@localhost:5432/basudebpuragrodb', echo=True)
            
        return dbEngine.dbengine