'''
Created on 30-Oct-2018

@author: tanumoy
'''
from util.db_helper import db_transaction
from model.User import User

@db_transaction
def get_user_type_by_user_id(user_id, session):
    return session.query(User).get(user_id).user_type