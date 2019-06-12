'''
Created on 25-Dec-2018

@author: duttasudip89
'''
from marshmallow.schema import Schema
from marshmallow import fields

class SupplierMasterHeaderSchema(Schema):
    '''
    classdocs
    '''
    
    supplier_code = fields.Str(required=True)
    supplier_name = fields.Str(required=True)
    description = fields.Str(missing='')
    supplier_type = fields.Str(required=True)
    remarks = fields.Str(required=True)
    enabled_flag = fields.Str(required=True)
    effective_from = fields.Date('%Y/%m/%d')
    effective_to = fields.Date('%Y/%m/%d')
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    supplier_master_sites = fields.List(fields.Nested('schema.SupplierMasterSchema.SupplierMasterLinesSchema'))
    
    
    
    
    
    
class SupplierMasterLinesSchema(Schema):
    '''
    classdocs
    '''
        
    supplier_site_code = fields.Str(required=True)
    supplier_site_address = fields.Str(required=True)
    phone_number1 = fields.Str(missing='')
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    inactive_date = fields.Date('%Y/%m/%d')
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
    
class SupplierMasterHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    supplier_id = fields.Int()
    supplier_code = fields.Str(required=True)
    supplier_name = fields.Str(required=True)
    description = fields.Str(missing='')
    supplier_type = fields.Str(required=True)
    remarks = fields.Str(missing='')
    enabled_flag = fields.Str(required=True)
    effective_from = fields.Date('%Y/%m/%d')
    effective_to = fields.Date('%Y/%m/%d')
    created_by = fields.Str()
    last_updated_by = fields.Str(required=True)
    supplier_master_sites = fields.Nested('schema.SupplierMasterSchema.SupplierMasterLinesUpdateSchema', many=True, required=True)
    
    
    
    
    
    
class SupplierMasterLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    supplier_site_id = fields.Int()    
    supplier_site_code = fields.Str(required=True)
    supplier_site_address = fields.Str(required=True)
    phone_number1 = fields.Str(missing='')
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    inactive_date = fields.Date('%Y/%m/%d')
    created_by = fields.Str()
    last_updated_by = fields.Str(required=True)    
