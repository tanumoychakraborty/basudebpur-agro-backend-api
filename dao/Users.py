'''
Created on 30-Oct-2018

@author: tanumoy
'''
from util.db_helper import db_transaction
from model.User import User
from sqlalchemy.sql.expression import and_
from falcon.http_error import HTTPError
from falcon import status_codes

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
    
@db_transaction
def create_user(raw_data, session):
    userObj = User()
    userObj.user_name = raw_data['user_name']
    userObj.description = raw_data['description']
    userObj.phone_number1 = raw_data['phone_number1']
    userObj.phone_number2 = raw_data['phone_number2']
    userObj.email = raw_data['email']
    userObj.password = raw_data['password']
    userObj.user_type = raw_data['user_type']
    userObj.effective_from = raw_data['effective_from']
    userObj.effective_to = raw_data['effective_to']
    userObj.created_by = raw_data['created_by']
    userObj.last_updated_by = raw_data['last_updated_by']
    userObj.employee_id = raw_data['employee_id']
    userObj.password_life_span = raw_data['password_life_span']
    session.add(userObj)
    
    return userObj

@db_transaction
def update_user(raw_data,session):
    user_name = raw_data['user_name']
    userObj = session.query(User).filter_by(user_name=user_name).first()
    if userObj is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="User Details does not exist")
    
    userObj.description = raw_data['description']
    userObj.phone_number1 = raw_data['phone_number1']
    userObj.phone_number2 = raw_data['phone_number2']
    userObj.email = raw_data['email']
    userObj.password = raw_data['password']
    userObj.user_type = raw_data['user_type']
    userObj.effective_from = raw_data['effective_from']
    userObj.effective_to = raw_data['effective_to']
    userObj.last_updated_by = raw_data['last_updated_by']
    userObj.employee_id = raw_data['employee_id']
    userObj.password_life_span = raw_data['password_life_span'] 
    
@db_transaction
def get_user_detail(user_name,session):
    userObj = session.query(User).filter_by(user_name=user_name).first()
    result = dict(userObj.__dict__)
    result.pop('_sa_instance_state')
    return result

@db_transaction
def search_user_details(params,page, page_size,session):
        resultL = []
        user_name = params.get('user_name',None)
        description = params.get('description',None)
        phone_number1 = params.get('phone_number1',None)
        user_type = params.get('user_type',None)
        
        userDetails = session.query(User.user_name,User.description,
                                           User.user_type,User.effective_from,User.phone_number1)
         
        conditions = []
        if user_name:
            conditions.append(User.user_name == user_name)
        if description:
            conditions.append(User.description == description)
        if phone_number1:
            conditions.append(User.phone_number1 == phone_number1)
        if user_type:
            conditions.append(User.user_type == user_type)    
            
                
        userDetails = userDetails.filter(and_(*conditions)).all()   
        
        if page_size:
            userDetails = userDetails.limit(page_size)
        if page: 
            userDetails = userDetails.offset(page*page_size) 
                  
        for userDetail in userDetails:
            dict ={ }
            dict['user_name'] = userDetail[0]
            dict['description'] = userDetail[1]
            dict['user_type'] = userDetail[2]
            dict['effective_from'] = userDetail[3]
            dict['phone_number1'] = userDetail[4]
            
            resultL.append(dict)    
                
        return resultL       