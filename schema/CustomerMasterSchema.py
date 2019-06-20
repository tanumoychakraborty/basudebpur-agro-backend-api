'''
Created on 06-Apr-2019

@author: duttasudip89
'''

from marshmallow.schema import Schema
from marshmallow import fields

class CustomerMasterHeaderSchema(Schema):
    '''
    classdocs
    '''
    customer_code = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    description = fields.Str(required=True)
    customer_type = fields.Str(required=True)
    remarks = fields.Str(required=True)
    enabled_flag = fields.Str(required=True)
    effective_from = fields.Date('%Y-%m-%d')
    effective_to = fields.Date('%Y-%m-%d')
    created_by = fields.Str(required=True)
    
    customer_master_sites = fields.Nested('schema.CustomerMasterSchema.CustomerMasterLinesSchema', many=True, required=True)
    
    
    
    
    
    
class CustomerMasterLinesSchema(Schema):
    '''
    classdocs
    '''
    
    customer_site_code = fields.Str(required=True)
    customer_address = fields.Str(required=True)
    phone_number1 = fields.Str(required=True)
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    effective_from = fields.Date('%Y-%m-%d')
    effective_to = fields.Date('%Y-%m-%d')
    created_by = fields.Str(required=True)
    
    
class CustomerMasterHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    customer_id = fields.Int()
    customer_code = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    description = fields.Str(required=True)
    customer_type = fields.Str(required=True)
    remarks = fields.Str(required=True)
    enabled_flag = fields.Str(required=True)
    effective_from = fields.Date('%Y-%m-%d')
    effective_to = fields.Date('%Y-%m-%d')
    created_by = fields.Str(required=True)
    customer_master_sites = fields.Nested('schema.CustomerMasterSchema.CustomerMasterLinesUpdateSchema', many=True, required=True)
    
    
    
    
    
    
class CustomerMasterLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    customer_site_id = fields.Int()
    customer_site_code = fields.Str(required=True)
    customer_address = fields.Str(required=True)
    phone_number1 = fields.Str(required=True)
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    effective_from = fields.Date('%Y-%m-%d')
    effective_to = fields.Date('%Y-%m-%d')
    created_by = fields.Str(required=True)
    