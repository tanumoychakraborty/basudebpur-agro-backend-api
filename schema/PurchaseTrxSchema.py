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
    
    purchase_trx_number = fields.Str(required=True, missing='')
    transaction_date = fields.Date('%d/%m/%Y')#fields.DateTime('%Y-%m-%dT%H:%M:%S+03:00')
    order_type = fields.Str(required=True)
    order_status = fields.Str(required=True)
    buyer_id = fields.Int(required=True)
    suppplier_id = fields.Int(required=True)
    amount = fields.Int(required=True)
    weighting_number = fields.Str(missing='')
    ref_doc = fields.Raw(missing=bytearray())
    created_by = fields.Int(required=True)
    last_updated_by = fields.Int(required=True)
    purchase_trx_lines = fields.Nested('schema.PurchaseTrxSchema.PurchaseTrxLinesSchema', many=True, required=True)
    
    
    
    
    
    
class PurchaseTrxLinesSchema(Schema):
    '''
    classdocs
    '''
        
    item_id = fields.Int(required=True)
    item_description = fields.Str(missing='')
    unit_price = fields.Int(required=True)
    quantity = fields.Int(required=True)
    receipt_unit_price = fields.Int(required=True)
    receipt_qty = fields.Int(required=True)
    unit_of_measure = fields.Str(missing='')
    line_status = fields.Str(missing='')
    created_by = fields.Int(required=True)
    last_updated_by = fields.Int(required=True)
    

class PurchaseTrxHeaderUpdateSchema(Schema):
    '''
    classdocs
    '''
    
    transaction_header_id = fields.Int(required=True)
    purchase_trx_number = fields.Str(required=True)
    transaction_date = fields.Date('%d/%m/%Y') #fields.DateTime('%Y-%m-%dT%H:%M:%S+03:00')
    order_type = fields.Str()
    order_status = fields.Str()
    buyer_id = fields.Int()
    suppplier_id = fields.Int()
    amount = fields.Int()
    weighting_number = fields.Str(missing='')
    ref_doc = fields.Raw(missing=bytearray())
    created_by = fields.Int()
    creation_date = fields.Str()
    last_updated_by = fields.Int()
    last_update_date = fields.Str()
    purchase_trx_lines = fields.Nested('schema.PurchaseTrxSchema.PurchaseTrxLinesUpdateSchema', many=True, required=True)
    

class PurchaseTrxLinesUpdateSchema(Schema):
    '''
    classdocs
    '''
    transaction_line_id = fields.Int(required=True)   
    transaction_header_id = fields.Int(required=True)
    item_id = fields.Int()
    item_description = fields.Str(missing='')
    unit_price = fields.Int()
    quantity = fields.Int()
    receipt_unit_price = fields.Int()
    receipt_qty = fields.Int()
    unit_of_measure = fields.Str(missing='')
    line_status = fields.Str(missing='')
    created_by = fields.Int()
    last_updated_by = fields.Int()
    creation_date = fields.Str()
    last_update_date = fields.Str()