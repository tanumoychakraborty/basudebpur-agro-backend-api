'''
Created on 07-Jul-2019

@author: duttasudip89
'''

from marshmallow.schema import Schema
from marshmallow import fields

class ReceiptHeaderSchema(Schema):
    '''
    classdocs
    '''
    receipt_number = fields.Str(required=True)
    challan_number = fields.Str()
    receipt_date = fields.DateTime('%Y-%m-%d')
    challan_date = fields.DateTime('%Y-%m-%d')
    source_transaction_header_id = fields.Int(required=True)
    source_transaction_type = fields.Str(required=True)
    vehicle_number = fields.Str(required=True)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    receipt_lines = fields.Nested('schema.ReceiptSchema.ReceiptLinesSchema', many=True, required=True)
   
    
    
    
class ReceiptLinesSchema(Schema):
    '''
    classdocs
    '''
        
    item_id = fields.Int(required=True)
    line_number = fields.Int(required=True)
    load_unload_number = fields.Str(missing='')
    load_unload_area = fields.Str(missing='')
    weighting_number = fields.Str(missing='')
    unit_of_measure  = fields.Str(required=True)
    receipt_line_status = fields.Str(missing='')
    quantity = fields.Float(missing=0)
    unit_price = fields.Float(missing=0)
    discount = fields.Float(missing=0)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    

class ReceiptHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    receipt_header_id = fields.Int()
    receipt_number = fields.Str(required=True)
    challan_number = fields.Str()
    receipt_date = fields.DateTime('%Y-%m-%d')
    challan_date = fields.DateTime('%Y-%m-%d')
    source_transaction_header_id = fields.Int(required=True)
    source_transaction_type = fields.Str(required=True)
    vehicle_number = fields.Str(required=True)
    #created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
    receipt_lines = fields.Nested('schema.ReceiptSchema.ReceiptLinesUpdateSchema', many=True, required=True)
    
    
    

class ReceiptLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    receipt_header_id = fields.Int()
    receipt_line_id = fields.Int()
    item_id = fields.Int(required=True)
    line_number = fields.Int(required=True)
    load_unload_number = fields.Str(missing='')
    load_unload_area = fields.Str(missing='')
    unit_of_measure  = fields.Str(required=True)
    weighting_number = fields.Str(missing='')
    receipt_line_status = fields.Str(missing='')
    quantity = fields.Float(missing=0)
    unit_price = fields.Float(missing=0)
    discount = fields.Float(missing=0)
    #created_by = fields.Str()
    last_updated_by = fields.Str(required=True)