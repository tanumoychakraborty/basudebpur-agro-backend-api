'''
Created on 28-Oct-2018

@author: tanumoy

Functions to access and manipulate Access Rights
'''
from util.db_helper import db_transaction
from model.AccessRights import AccessRights

@db_transaction
def get_access_rights_by_user_type(usertype, session):
    result = []
    accesses = session.query(AccessRights).filter_by(user_type=usertype).all()
    for row in accesses:
        rowdict = dict(row.__dict__)
        rowdict.pop('_sa_instance_state')
        result.append(rowdict)
            
    return result
# if __name__ == '__main__':
#     get_access_rights_by_access_id(10)