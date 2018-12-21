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
def get_purchase_order_header_status(lookupName,session):
    resultL = []
    headerStatus = session.query(CommonLookups.meaning).filter(CommonLookups.lookup_name==lookupName,CommonLookups.enabled=='Y').all()
    for row in headerStatus:
        dict ={ }
        dict['meaning'] = row[0]
        
        resultL.append(dict)
    return resultL        
            