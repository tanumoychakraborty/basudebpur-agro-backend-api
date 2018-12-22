'''
Created on 21-Dec-2018

@author: duttasudip89
'''
'''
Functions to fetch common lookup utilities
'''
from util.db_helper import db_transaction
from model.CommonLookups import CommonLookups

@db_transaction
def get_lookup_values(lookupName,session):
    resultL = []
    lookupValues = session.query(CommonLookups.meaning,CommonLookups.lookup_code).filter(CommonLookups.lookup_name==lookupName,CommonLookups.enabled=='Y').all()
    for row in lookupValues:
        dict ={ }
        dict['meaning'] = row[0]
        dict['lookup_code'] = row[1]
        
        resultL.append(dict)
    return resultL        
            