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
    customer_name = fields.Str(required=False)
    description = fields.Str(missing='')
    customer_type = fields.Str(required=False)
    remarks = fields.Str(missing='')
    enabled_flag = fields.Str(required=False)
    effective_from = fields.Date('%Y-%m-%d', required=False)
    effective_to = fields.Date('%Y-%m-%d', required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    customer_master_sites = fields.Nested('schema.CustomerMasterSchema.CustomerMasterLinesSchema', many=True, required=False)
    
    
    
    
    
    
class CustomerMasterLinesSchema(Schema):
    '''
    classdocs
    '''
    
    customer_site_code = fields.Str(required=False)
    customer_address = fields.Str(missing='')
    phone_number1 = fields.Str(missing='')
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    effective_from = fields.Date('%Y-%m-%d', required=False)
    effective_to = fields.Date('%Y-%m-%d', required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
    
class CustomerMasterHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    customer_id = fields.Int()
    customer_code = fields.Str(required=False)
    customer_name = fields.Str(required=False)
    description = fields.Str(missing='')
    customer_type = fields.Str(required=False)
    remarks = fields.Str(missing='')
    enabled_flag = fields.Str(required=False)
    effective_from = fields.Date('%Y-%m-%d', required=False)
    effective_to = fields.Date('%Y-%m-%d', required=False)
    created_by = fields.Str(required=False)
    last_updated_by = fields.Str(required=True)
    customer_master_sites = fields.Nested('schema.CustomerMasterSchema.CustomerMasterLinesUpdateSchema', many=True, required=False)
    
    
    
    
    
    
class CustomerMasterLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    customer_site_id = fields.Int()
    customer_site_code = fields.Str(required=False)
    customer_address = fields.Str(missing='')
    phone_number1 = fields.Str(missing='')
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    effective_from = fields.Date('%Y-%m-%d', required=False)
    effective_to = fields.Date('%Y-%m-%d', required=False)
    created_by = fields.Str(required=False)
    last_updated_by = fields.Str(required=True)
    