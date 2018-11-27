'''
Created on 26-Nov-2018

@author: tanumoy
'''
from model.PurchaseTrxHeader import PurchaseTrxHeader
from model.PurchaseTrxLines import PurchaseTrxLines
from util.db_helper import db_transaction
from datetime import datetime

@db_transaction
def create_purchase_trx(raw_data, session):
    purchasetrxheader = PurchaseTrxHeader()
    if 'purchase_trx_number' in raw_data:
        purchasetrxheader.purchase_trx_number = raw_data['purchase_trx_number']
    if 'transaction_date' in raw_data:
        purchasetrxheader.transaction_date=raw_data['transaction_date']
    if 'order_type' in raw_data:
        purchasetrxheader.order_type=raw_data['order_type']
    if 'order_status' in raw_data:
        purchasetrxheader.order_status=raw_data['order_status']
    if 'buyer_id' in raw_data:
        purchasetrxheader.buyer_id=raw_data['buyer_id']
    if 'suppplier_id' in raw_data:
        purchasetrxheader.suppplier_id=raw_data['suppplier_id']
    if 'amount' in raw_data:
        purchasetrxheader.amount=raw_data['amount']
    if 'ref_doc' in raw_data:
        purchasetrxheader.weighting_number=raw_data['weighting_number']
    if 'created_by' in raw_data:
        purchasetrxheader.created_by=raw_data['created_by']
    if 'last_updated_by' in raw_data:
        purchasetrxheader.last_updated_by=raw_data['last_updated_by']
        
    purchasetrxLines = PurchaseTrxLines()
    if 'item_id' in raw_data:
        purchasetrxLines.item_id = raw_data['item_id']
    if 'item_description' in raw_data:
        purchasetrxLines.item_description=raw_data['item_description']
    if 'unit_price' in raw_data:
        purchasetrxLines.unit_price=raw_data['unit_price']
    if 'quantity' in raw_data:
        purchasetrxLines.quantity=raw_data['quantity']
    if 'receipt_unit_price' in raw_data:
        purchasetrxLines.receipt_unit_price=raw_data['receipt_unit_price']
    if 'receipt_qty' in raw_data:
        purchasetrxLines.receipt_qty=raw_data['receipt_qty']
    if 'unit_of_measure' in raw_data:
        purchasetrxLines.unit_of_measure=raw_data['unit_of_measure']
    if 'line_status' in raw_data:
        purchasetrxLines.line_status=raw_data['line_status']
    if 'created_by' in raw_data:
        purchasetrxLines.created_by=raw_data['created_by']
    if 'last_updated_by' in raw_data:
        purchasetrxLines.last_updated_by=raw_data['last_updated_by']   
     
    session.add(purchasetrxLines)
    
    return purchasetrxheader