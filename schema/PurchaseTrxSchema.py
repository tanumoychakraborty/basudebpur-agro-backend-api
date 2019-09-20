'''
Created on 28-Nov-2018

@author: tanumoy
'''
from marshmallow.schema import Schema
from marshmallow import fields

class PurchaseTrxHeaderSchema(Schema):
    '''
    classdocs
    '''
    
    transaction_date = fields.DateTime('%Y-%m-%d')#fields.DateTime('%Y-%m-%dT%H:%M:%S+03:00')
    order_status = fields.Str(required=False)
    buyer_id = fields.Str(required=True)
    supplier_id = fields.Int(required=False)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    purchase_trx_lines = fields.Nested('schema.PurchaseTrxSchema.PurchaseTrxLinesSchema', many=True, required=False)
    
    
    
class PurchaseTrxLinesSchema(Schema):
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
    

class PurchaseTrxHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    transaction_header_id = fields.Int(required=False)
    purchase_trx_number = fields.Str(required=True)
    transaction_date = fields.DateTime('%Y-%m-%d',required=False )#:%S+03:00
    order_status = fields.Str(required=False)
    buyer_id = fields.Str(required=False)
    buyer_name = fields.Str(required=False)
    supplier_id = fields.Int(required=False)
    amount = fields.Float(required=False)
    #created_by = fields.Int()
    #creation_date = fields.Str()
    last_updated_by = fields.Str(required=True)
    #last_update_date = fields.Str()
    purchase_trx_lines = fields.Nested('schema.PurchaseTrxSchema.PurchaseTrxLinesUpdateSchema', many=True, required=False)
    

class PurchaseTrxLinesUpdateSchema(Schema):
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
    
    
    