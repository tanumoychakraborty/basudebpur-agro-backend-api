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
    bata = fields.Float(required=False)
    net_weight = fields.Float(required=False)
    average_weight = fields.Float(required=False)
    total_bags = fields.Float(required=False)
    unit_of_measure  = fields.Str(required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=False)
    #receipt_header_status = fields.Str(required=True)
    receipt_lines = fields.Nested('schema.ReceiptSchema.ReceiptLinesSchema', many=True, required=False)
   
    
    
    
class ReceiptLinesSchema(Schema):
    '''
    classdocs
    '''
        
    item_id = fields.Int(required=False)
    line_number = fields.Int(required=False)
    load_unload_number = fields.Str(required=False)
    description = fields.Str(required=False)
    load_unload_area = fields.Str(required=False)
    weighing_number = fields.Str(required=False)
    unit_of_measure  = fields.Str(required=False)
    receipt_line_status = fields.Str(missing='OPEN')
    quantity = fields.Float(required=False)
    number_of_bags = fields.Float(required=False)
    unit_price = fields.Float(required=False)
    discount = fields.Float(required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=False)
    

class ReceiptHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    receipt_header_id = fields.Int(required=False)
    receipt_number = fields.Str(required=False)
    challan_number = fields.Str(required=True)
    receipt_date = fields.DateTime('%Y-%m-%d')
    challan_date = fields.DateTime('%Y-%m-%d')
    source_transaction_header_id = fields.Str(required=False)
    source_transaction_type = fields.Str(required=False)
    vehicle_number = fields.Str(required=False)
    bata = fields.Float(required=False)
    net_weight = fields.Float(required=False)
    average_weight = fields.Float(required=False)
    total_bags = fields.Float(required=False)
    unit_of_measure  = fields.Str(required=False)
    receipt_header_status = fields.Str(required=False)
    #created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    
    receipt_lines = fields.Nested('schema.ReceiptSchema.ReceiptLinesUpdateSchema', many=True, required=False)
    
    
    

class ReceiptLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    receipt_header_id = fields.Int()
    receipt_line_id = fields.Int(required=False)
    item_id = fields.Int(required=False)
    description = fields.Str(required=False)
    line_number = fields.Int(required=False)
    load_unload_number = fields.Str(required=False)
    load_unload_area = fields.Str(required=False)
    unit_of_measure  = fields.Str(required=False)
    weighing_number = fields.Str(missing='')
    receipt_line_status = fields.Str(missing='OPEN')
    quantity = fields.Float(required=False)
    number_of_bags = fields.Float(required=False)
    unit_price = fields.Float(required=False)
    discount = fields.Float(required=False)
    #created_by = fields.Str()
    last_updated_by = fields.Str(required=False)
    
    
    