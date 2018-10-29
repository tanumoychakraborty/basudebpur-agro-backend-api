'''
Created on 28-Oct-2018

@author: tanumoy

Functions to access and manipulate Access Rights
'''
from util.db_helper import db_transaction
from model.AccessRights import AccessRights

@db_transaction
def get_access_rights_by_access_id(access_id, session):
    print(session)
    return session.query(AccessRights).get(access_id)

# if __name__ == '__main__':
#     get_access_rights_by_access_id(10)