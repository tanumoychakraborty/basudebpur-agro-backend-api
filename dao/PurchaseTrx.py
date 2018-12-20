'''
Created on 26-Nov-2018

@author: tanumoy
'''
from model.PurchaseTrxHeader import PurchaseTrxHeader
from model.PurchaseTrxLines import PurchaseTrxLines
from model.SupplierMasterHeader import SupplierMasterHeader
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
    purchasetrxheader.vehicle_number = raw_data['vehicle_number']
    purchasetrxheader.created_by = raw_data['created_by']
    purchasetrxheader.last_updated_by = raw_data['last_updated_by']
        
    purchasetrxLines = []
    for purchase_trx_line in raw_data['purchase_trx_lines']:
        purchasetrxLine = PurchaseTrxLines()
        purchasetrxLine.item_id = purchase_trx_line['item_id']
        purchasetrxLine.line_number = purchase_trx_line['line_number']
        purchasetrxLine.item_description = purchase_trx_line['item_description']
        purchasetrxLine.booking_unit_price = purchase_trx_line['booking_unit_price']
        purchasetrxLine.booking_quantity = purchase_trx_line['booking_quantity']
        purchasetrxLine.receipt_unit_price = purchase_trx_line['receipt_unit_price']
        purchasetrxLine.receipt_quantity = purchase_trx_line['receipt_quantity']
        purchasetrxLine.unit_of_measure = purchase_trx_line['unit_of_measure']
        purchasetrxLine.discount = purchase_trx_line['discount']
        purchasetrxLine.line_status = purchase_trx_line['line_status']
        purchasetrxLine.created_by = purchase_trx_line['created_by']
        purchasetrxLine.last_updated_by = purchase_trx_line['last_updated_by']   
        purchasetrxLines.append(purchasetrxLine)
            
    purchasetrxheader.purchase_trx_lines = purchasetrxLines
     
    session.add(purchasetrxheader)
    
    return purchasetrxheader

@db_transaction
def get_purchase_transaction_details(params,page, page_size,session):
    resultL = []
    if params is None:
        purchaseTrxDetails = session.query(PurchaseTrxHeader.purchase_trx_number,PurchaseTrxHeader.transaction_date,
                                           SupplierMasterHeader.supplier_name,PurchaseTrxHeader.amount,PurchaseTrxHeader.order_type,PurchaseTrxHeader.order_status,
                                           PurchaseTrxHeader.weighting_number).join(SupplierMasterHeader,PurchaseTrxHeader.suppplier_id==SupplierMasterHeader.supplier_id).limit(500).all
        if page_size:
            purchaseTrxDetails = purchaseTrxDetails.limit(page_size)
        if page: 
            purchaseTrxDetails = purchaseTrxDetails.offset(page*page_size)
    else:
        setwherecaluse1 = ''"'NA'"''
        setwherecaluse2 = ''"'NA'"''
        setwherecaluse = setwherecaluse1 +'='+setwherecaluse2
        purchase_trx_number = params['purchase_trx_number']
        supplier_id = params['supplier_id']
        transaction_date = params['transaction_date']
        weighting_number = params['weighting_number']
        buyer_id = params['buyer_id']
        from_creation_date = params['from_creation_date']
        to_creation_date = params['to_creation_date']
        
                
        
        
        
        purchaseTrxDetails = session.query(PurchaseTrxHeader.purchase_trx_number,PurchaseTrxHeader.transaction_date
                                           ,SupplierMasterHeader.supplier_name,PurchaseTrxHeader.amount,PurchaseTrxHeader.order_type,PurchaseTrxHeader.order_status
                                           ,PurchaseTrxHeader.weighting_number).join(SupplierMasterHeader,PurchaseTrxHeader.suppplier_id==SupplierMasterHeader.supplier_id).filter(PurchaseTrxHeader.purchase_trx_number== purchase_trx_number).all()
         
        
        if page_size:
            purchaseTrxDetails = purchaseTrxDetails.limit(page_size)
        if page: 
            purchaseTrxDetails = purchaseTrxDetails.offset(page*page_size) 
                  
    for purchaseTrxDetail in purchaseTrxDetails:
        dict ={ }
        dict['purchase_trx_number'] = purchaseTrxDetail[0]
        dict['transaction_date'] = purchaseTrxDetail[1]
        dict['supplier_name'] = purchaseTrxDetail[2]
        dict['amount'] = purchaseTrxDetail[3]
        dict['order_status'] = purchaseTrxDetail[4]
        dict['order_type'] = purchaseTrxDetail[5]
        dict['weighting_number'] = purchaseTrxDetail[6]
        
        resultL.append(dict)    
            
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
    purchasetrxheader.vehicle_number = raw_data['vehicle_number']
    purchasetrxheader.last_updated_by = raw_data['last_updated_by']
        
    for purchase_trx_line in raw_data['purchase_trx_lines']:
        for trx_line in purchasetrxheader.purchase_trx_lines:
            if purchase_trx_line["transaction_line_id"] == trx_line.transaction_line_id:
                trx_line.item_id = purchase_trx_line['item_id']
                trx_line.line_number = purchase_trx_line['line_number']
                trx_line.item_description = purchase_trx_line['item_description']
                trx_line.booking_unit_price = purchase_trx_line['booking_unit_price']
                trx_line.booking_quantity = purchase_trx_line['booking_quantity']
                trx_line.receipt_unit_price = purchase_trx_line['receipt_unit_price']
                trx_line.receipt_quantity = purchase_trx_line['receipt_quantity']
                trx_line.unit_of_measure = purchase_trx_line['unit_of_measure']
                trx_line.discount = purchase_trx_line['discount']
                trx_line.line_status = purchase_trx_line['line_status']
                trx_line.created_by = purchase_trx_line['created_by']
                trx_line.last_updated_by = purchase_trx_line['last_updated_by']   
            
