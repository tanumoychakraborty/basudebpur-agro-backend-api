'''
Created on 22-Sep-2019

@author: duttasudip89
'''
from marshmallow.schema import Schema
from marshmallow import fields

class InventoryItemsSchema(Schema):
    '''
    classdocs
    '''
    
    item_number = fields.Str(required=True)
    description = fields.Str(required=False)
    enabled_flag = fields.Str(required=False)
    item_type = fields.Str(required=True)
    long_description = fields.Str(required=False)
    transaction_uom = fields.Str(required=False)
    conversion = fields.Float(required=False)
    base_uom = fields.Str(required=False)
    
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
class InventoryItemsUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    item_id = fields.Int()
    item_number = fields.Str(required=True)
    description = fields.Str(required=False)
    enabled_flag = fields.Str(required=False)
    item_type = fields.Str(required=True)
    long_description = fields.Str(required=False)
    transaction_uom = fields.Str(required=False)
    conversion = fields.Float(required=False)
    base_uom = fields.Str(required=False)
    last_updated_by = fields.Str(required=True)    
     
    
    
    
