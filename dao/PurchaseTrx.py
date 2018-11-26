'''
Created on 26-Nov-2018

@author: tanumoy
'''
from model.PurchaseTrxHeader import PurchaseTrxHeader
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
     
    session.add(purchasetrxheader)
    
    return purchasetrxheader