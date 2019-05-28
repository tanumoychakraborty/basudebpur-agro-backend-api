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
    purchase_trx_number = fields.Str(required=True)
    transaction_date = fields.DateTime('%Y/%m/%dT%H:%M')#fields.DateTime('%Y-%m-%dT%H:%M:%S+03:00')
    order_type = fields.Str(required=True)
    order_status = fields.Str(required=True)
    buyer_id = fields.Str(required=True)
    supplier_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    purchase_trx_lines = fields.Nested('schema.PurchaseTrxSchema.PurchaseTrxLinesSchema', many=True, required=True)
    
    
    
class PurchaseTrxLinesSchema(Schema):
    '''
    classdocs
    '''
        
    item_id = fields.Int(required=True)
    line_number = fields.Int(required=True)
    item_description = fields.Str(missing='')
    booking_unit_price = fields.Float(missing=0)
    booking_quantity = fields.Float(missing=0)
    unit_of_measure = fields.Str(missing='')
    discount = fields.Float(missing=0)
    created_by = fields.Str(required=True)
    last_updated_by = fields.Str(required=True)
    

class PurchaseTrxHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    transaction_header_id = fields.Int()
    purchase_trx_number = fields.Str(required=True)
    transaction_date = fields.DateTime('%Y/%m/%dT%H:%M')#:%S+03:00
    order_type = fields.Str()
    order_status = fields.Str()
    buyer_id = fields.Str()
    supplier_id = fields.Int()
    amount = fields.Float()
    created_by = fields.Int()
    #creation_date = fields.Str()
    last_updated_by = fields.Str(required=True)
    #last_update_date = fields.Str()
    purchase_trx_lines = fields.Nested('schema.PurchaseTrxSchema.PurchaseTrxLinesUpdateSchema', many=True, required=True)
    

class PurchaseTrxLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    transaction_line_id = fields.Int()   
    transaction_header_id = fields.Int()
    item_id = fields.Int(required=True)
    line_number = fields.Int(required=True)
    item_description = fields.Str(missing='')
    booking_unit_price = fields.Float(missing=0)
    booking_quantity = fields.Float(missing=0)
    unit_of_measure = fields.Str()
    discount = fields.Float(missing=0)
    created_by = fields.Str()
    last_updated_by = fields.Str(required=True)