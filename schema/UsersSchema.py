'''
Created on 03-Jan-2019

@author: duttasudip89
'''

from marshmallow.schema import Schema
from marshmallow import fields

class UsersSchema(Schema):
    '''
    classdocs
    '''
    
    user_name = fields.Str(required=True)
    description = fields.Str()
    phone_number1 = fields.Str(required=True)
    phone_number2 = fields.Str()
    email = fields.Str()
    password = fields.Str(required=True)
    user_type= fields.Str(required=True)
    effective_from = fields.Date('%Y-%m-%d')
    effective_to = fields.Date('%Y-%m-%d')
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    password_life_span = fields.Str()
    employee_id = fields.Str()
    
    
class UsersSchemaUpdate(Schema):
    '''
    classdocs
    '''
    
    user_name = fields.Str(required=True)
    description = fields.Str()
    phone_number1 = fields.Str(required=True)
    phone_number2 = fields.Str()
    email = fields.Str()
    password = fields.Str(required=True)
    user_type= fields.Str(required=True)
    effective_from = fields.Date('%Y-%m-%d')
    effective_to = fields.Date('%Y-%m-%d')
    last_updated_by = fields.Str(required=True)
    password_life_span = fields.Str()
    employee_id = fields.Str()    