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
    receipt_number = fields.Str(required=False)
    challan_number = fields.Str()
    receipt_date = fields.DateTime('%Y-%m-%d')
    challan_date = fields.DateTime('%Y-%m-%d')
    source_transaction_header_id = fields.Str(required=False)
    source_transaction_type = fields.Str(required=False)
    vehicle_number = fields.Str(required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=False)
    receipt_lines = fields.Nested('schema.ReceiptSchema.ReceiptLinesSchema', many=True, required=False)
   
    
    
    
class ReceiptLinesSchema(Schema):
    '''
    classdocs
    '''
        
    item_id = fields.Int(required=False)
    line_number = fields.Int(required=False)
    load_unload_number = fields.Str(missing='')
    load_unload_area = fields.Str(missing='')
    weighing_number = fields.Str(missing='')
    unit_of_measure  = fields.Str(required=False)
    receipt_line_status = fields.Str(missing='')
    quantity = fields.Float(missing=0)
    unit_price = fields.Float(missing=0)
    discount = fields.Float(missing=0)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=False)
    

class ReceiptHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    receipt_header_id = fields.Int()
    receipt_number = fields.Str(required=False)
    challan_number = fields.Str()
    receipt_date = fields.DateTime('%Y-%m-%d')
    challan_date = fields.DateTime('%Y-%m-%d')
    source_transaction_header_id = fields.Int(required=False)
    source_transaction_type = fields.Str(required=False)
    vehicle_number = fields.Str(required=False)
    #created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
    receipt_lines = fields.Nested('schema.ReceiptSchema.ReceiptLinesUpdateSchema', many=True, required=True)
    
    
    

class ReceiptLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    receipt_header_id = fields.Int()
    receipt_line_id = fields.Int()
    item_id = fields.Int(required=False)
    line_number = fields.Int(required=False)
    load_unload_number = fields.Str(missing='')
    load_unload_area = fields.Str(missing='')
    unit_of_measure  = fields.Str(required=False)
    weighing_number = fields.Str(missing='')
    receipt_line_status = fields.Str(missing='')
    quantity = fields.Float(missing=0)
    unit_price = fields.Float(missing=0)
    discount = fields.Float(missing=0)
    #created_by = fields.Str()
    last_updated_by = fields.Str(required=False)