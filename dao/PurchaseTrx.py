'''
Created on 26-Nov-2018

@author: tanumoy
'''
from model.PurchaseTrxHeader import PurchaseTrxHeader
from model.PurchaseTrxLines import PurchaseTrxLines
from util.db_helper import db_transaction


@db_transaction
def create_purchase_trx(raw_data, session):
    purchasetrxheader = PurchaseTrxHeader()
    purchasetrxheader.purchase_trx_number = raw_data['purchase_trx_number']
    purchasetrxheader.transaction_date = raw_data['transaction_date']
    purchasetrxheader.order_type = raw_data['order_type']
    purchasetrxheader.order_status = raw_data['order_status']
    purchasetrxheader.buyer_id = raw_data['buyer_id']
    purchasetrxheader.suppplier_id = raw_data['suppplier_id']
    purchasetrxheader.amount = raw_data['amount']
    purchasetrxheader.ref_doc = raw_data['ref_doc']
    purchasetrxheader.weighting_number = raw_data['weighting_number']
    purchasetrxheader.created_by = raw_data['created_by']
    purchasetrxheader.last_updated_by = raw_data['last_updated_by']
        
    purchasetrxLines = []
    for purchase_trx_line in raw_data['purchase_trx_lines']:
        purchasetrxLine = PurchaseTrxLines()
        purchasetrxLine.item_id = purchase_trx_line['item_id']
        purchasetrxLine.item_description = purchase_trx_line['item_description']
        purchasetrxLine.unit_price = purchase_trx_line['unit_price']
        purchasetrxLine.quantity = purchase_trx_line['quantity']
        purchasetrxLine.receipt_unit_price = purchase_trx_line['receipt_unit_price']
        purchasetrxLine.receipt_qty = purchase_trx_line['receipt_qty']
        purchasetrxLine.unit_of_measure = purchase_trx_line['unit_of_measure']
        purchasetrxLine.line_status = purchase_trx_line['line_status']
        purchasetrxLine.created_by = purchase_trx_line['created_by']
        purchasetrxLine.last_updated_by = purchase_trx_line['last_updated_by']   
        purchasetrxLines.append(purchasetrxLine)
            
    purchasetrxheader.purchase_trx_lines = purchasetrxLines
     
    session.add(purchasetrxheader)
    
    return purchasetrxheader

@db_transaction
def get_purchase_transaction_details(params, session):
    resultL = []
    if params is None:
        purchaseTrxDetails = session.query(PurchaseTrxHeader).all()
    else:
        purchase_trx_number = params['purchase_trx_number']
        purchaseTrxDetails = session.query(PurchaseTrxHeader).filter_by(purchase_trx_number=purchase_trx_number).all()
    
    for purchaseTrxDetail in purchaseTrxDetails:
        rowdict = dict(purchaseTrxDetail.__dict__)
        rowdict.pop('_sa_instance_state')
        purchaseLines = purchaseTrxDetail.purchase_trx_lines
        
        linedict = []
        for  purchaseLine in purchaseLines:
            line = dict(purchaseLine.__dict__)
            line.pop('_sa_instance_state')
            linedict.append(line)
        
        rowdict['purchase_trx_lines']= linedict
        
        resultL.append(rowdict)
            
    return resultL



@db_transaction
def update_purchase_trx(raw_data,session):
    purchase_trx_number = raw_data['purchase_trx_number']
    purchasetrxheader = session.query(PurchaseTrxHeader).filter_by(purchase_trx_number=purchase_trx_number).first()
    
    purchasetrxheader.transaction_date = raw_data['transaction_date']
    purchasetrxheader.order_type = raw_data['order_type']
    purchasetrxheader.order_status = raw_data['order_status']
    purchasetrxheader.buyer_id = raw_data['buyer_id']
    purchasetrxheader.suppplier_id = raw_data['suppplier_id']
    purchasetrxheader.amount = raw_data['amount']
    '''
    do it later
    purchasetrxheader.ref_doc = raw_data['ref_doc']
    '''
    purchasetrxheader.weighting_number = raw_data['weighting_number']
    purchasetrxheader.last_updated_by = raw_data['last_updated_by']
        
    for purchase_trx_line in raw_data['purchase_trx_lines']:
        for trx_line in purchasetrxheader.purchase_trx_lines:
            if purchase_trx_line["transaction_line_id"] == trx_line.transaction_line_id:
                trx_line.item_id = purchase_trx_line['item_id']
                trx_line.item_description = purchase_trx_line['item_description']
                trx_line.unit_price = purchase_trx_line['unit_price']
                trx_line.quantity = purchase_trx_line['quantity']
                trx_line.receipt_unit_price = purchase_trx_line['receipt_unit_price']
                trx_line.receipt_qty = purchase_trx_line['receipt_qty']
                trx_line.unit_of_measure = purchase_trx_line['unit_of_measure']
                trx_line.line_status = purchase_trx_line['line_status']
                trx_line.created_by = purchase_trx_line['created_by']
                trx_line.last_updated_by = purchase_trx_line['last_updated_by']   
            
