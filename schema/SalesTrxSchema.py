'''
Created on 28-Nov-2018

@author: tanumoy
'''
from marshmallow.schema import Schema
from marshmallow import fields

class SalesTrxHeaderSchema(Schema):
    '''
    classdocs
    '''
    
    transaction_date = fields.DateTime('%Y-%m-%d', required=False)#fields.DateTime('%Y-%m-%dT%H:%M:%S+03:00')
    order_status = fields.Str(required=False)
    sales_rep_id = fields.Str(required=True)
    customer_id = fields.Int(required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    sales_trx_lines = fields.Nested('schema.SalesTrxSchema.SalesTrxLinesSchema', many=True, required=False)
    
    
    
class SalesTrxLinesSchema(Schema):
    '''
    classdocs
    '''
        
    item_id = fields.Int(required=False)
    line_number = fields.Int(required=False)
    item_description = fields.Str(required=False)
    booking_unit_price = fields.Float(required=False)
    booking_quantity = fields.Float(required=False)
    unit_of_measure = fields.Str(required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    

class SalesTrxHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    transaction_header_id = fields.Int(required=False)
    sales_trx_number = fields.Str(required=True)
    transaction_date = fields.DateTime('%Y-%m-%d',required=False )#:%S+03:00
    order_status = fields.Str(required=False)
    sales_rep_id = fields.Str(required=False)
    sales_rep_name = fields.Str(required=False)
    customer_id = fields.Int(required=False)
    amount = fields.Float(required=False)
    last_updated_by = fields.Str(required=True)
    sales_trx_lines = fields.Nested('schema.SalesTrxSchema.SalesTrxLinesUpdateSchema', many=True, required=False)
    

class SalesTrxLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    transaction_line_id = fields.Int(required=False)   
    transaction_header_id = fields.Int(required=False)
    item_id = fields.Int(required=False)
    line_number = fields.Int(required=False)
    booking_unit_price = fields.Float(required=False)
    booking_quantity = fields.Float(required=False)
    unit_of_measure = fields.Str(required=False)
    created_by = fields.Str(required=False)
    last_updated_by = fields.Str(required=True)
    
    
    