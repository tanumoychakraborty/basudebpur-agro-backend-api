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
    supplier_name = fields.Str(required=False)
    description = fields.Str(required=False)
    supplier_type = fields.Str(required=False)
    remarks = fields.Str(required=False)
    enabled_flag = fields.Str(required=False)
    effective_from = fields.Date('%Y-%m-%d',required=False)
    effective_to = fields.Date('%Y-%m-%d',required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    supplier_master_sites = fields.List(fields.Nested('schema.SupplierMasterSchema.SupplierMasterLinesSchema'),many=True,required=False)
    
    
    
    
    
    
class SupplierMasterLinesSchema(Schema):
    '''
    classdocs
    '''
        
    supplier_site_code = fields.Str(required=False)
    supplier_site_address = fields.Str(required=False)
    phone_number1 = fields.Str(required=False)
    phone_number2 = fields.Str(required=False)
    email = fields.Str(required=False)
    inactive_date = fields.Date('%Y/%m/%d',required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
    
class SupplierMasterHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    supplier_id = fields.Int()
    supplier_code = fields.Str(required=False)
    supplier_name = fields.Str(required=False)
    description = fields.Str(missing='')
    supplier_type = fields.Str(required=True)
    remarks = fields.Str(missing='')
    enabled_flag = fields.Str(required=False)
    effective_from = fields.Date('%Y-%m-%d',required=False)
    effective_to = fields.Date('%Y-%m-%d',required=False)
    created_by = fields.Str()
    last_updated_by = fields.Str(required=True)
    supplier_master_sites = fields.Nested('schema.SupplierMasterSchema.SupplierMasterLinesUpdateSchema', many=True, required=False)
    
    
    
    
    
    
class SupplierMasterLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    supplier_site_id = fields.Int()    
    supplier_site_code = fields.Str(required=False)
    supplier_site_address = fields.Str(required=False)
    phone_number1 = fields.Str(missing='')
    phone_number2 = fields.Str(missing='')
    email = fields.Str(missing='')
    inactive_date = fields.Date('%Y-%m-%d',required=False)
    created_by = fields.Str()
    last_updated_by = fields.Str(required=True)    
