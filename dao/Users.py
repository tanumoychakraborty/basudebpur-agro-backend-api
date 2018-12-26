'''
Created on 30-Oct-2018

@author: tanumoy
'''
from util.db_helper import db_transaction
from model.User import User

@db_transaction
def get_user_type_by_user_id(user_id, session):
    try:
        return session.query(User).get(user_id).user_type
    except AttributeError:
        return None

@db_transaction
def get_user_id_by_user_name(user_name, session):
    try:
        return session.query(User).filter_by(user_name=user_name).first().user_id
    except AttributeError:
        return None

@db_transaction
def get_user_type_by_username_password(username, password, session):
    try:
        return session.query(User).filter_by(user_name=username, password=password).first().user_type
    except AttributeError:
        return None