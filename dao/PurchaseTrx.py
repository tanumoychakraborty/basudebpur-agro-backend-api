'''
Created on 26-Nov-2018

@author: tanumoy
'''
from model.PurchaseTrxHeader import PurchaseTrxHeader
from model.PurchaseTrxLines import PurchaseTrxLines
from model.SupplierMasterHeader import SupplierMasterHeader
from util.db_helper import db_transaction
from sqlalchemy.sql.expression import and_


@db_transaction
def create_purchase_trx(raw_data, session):
    purchasetrxheader = PurchaseTrxHeader()
    purchasetrxheader.purchase_trx_number = raw_data['purchase_trx_number']
    purchasetrxheader.transaction_date = raw_data['transaction_date']
    purchasetrxheader.order_type = raw_data['order_type']
    purchasetrxheader.order_status = raw_data['order_status']
    purchasetrxheader.buyer_id = raw_data['buyer_id']
    purchasetrxheader.supplier_id = raw_data['supplier_id']
    purchasetrxheader.amount = raw_data['amount']
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
        purchasetrxLine.unit_of_measure = purchase_trx_line['unit_of_measure']
        purchasetrxLine.discount = purchase_trx_line['discount']
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
                                           SupplierMasterHeader.supplier_name,PurchaseTrxHeader.amount,PurchaseTrxHeader.order_type,PurchaseTrxHeader.order_status).join(SupplierMasterHeader,PurchaseTrxHeader.supplier_id==SupplierMasterHeader.supplier_id).limit(500).all()
        if page_size:
            purchaseTrxDetails = purchaseTrxDetails.limit(page_size)
        if page: 
            purchaseTrxDetails = purchaseTrxDetails.offset(page*page_size)
    else:
        purchase_trx_number = params.get('purchase_trx_number',None)
        supplier_id = params.get('supplier_id',None)
        transaction_date = params.get('transaction_date',None)
        buyer_id = params.get('buyer_id',None)
        from_creation_date = params.get('from_creation_date',None)
        to_creation_date = params.get('to_creation_date',None)
        order_status = params.get('order_status',None)
        
        purchaseTrxDetails = session.query(PurchaseTrxHeader.purchase_trx_number,PurchaseTrxHeader.transaction_date
                                           ,SupplierMasterHeader.supplier_name,PurchaseTrxHeader.amount,PurchaseTrxHeader.order_type,PurchaseTrxHeader.order_status).join(SupplierMasterHeader,PurchaseTrxHeader.supplier_id==SupplierMasterHeader.supplier_id)
         
        conditions = []
        if purchase_trx_number:
            conditions.append(PurchaseTrxHeader.purchase_trx_number == purchase_trx_number)
        if supplier_id:
            conditions.append(PurchaseTrxHeader.supplier_id == supplier_id)
        if transaction_date:
            conditions.append(PurchaseTrxHeader.transaction_date == transaction_date)
        if buyer_id:
            conditions.append(PurchaseTrxHeader.buyer_id == buyer_id)
        if from_creation_date:
            conditions.append(PurchaseTrxHeader.creation_date >= from_creation_date)
        if to_creation_date:
            conditions.append(PurchaseTrxHeader.creation_date <= to_creation_date)    
        if order_status:
            conditions.append(PurchaseTrxHeader.order_status == order_status)            
                
            
                
        purchaseTrxDetails = purchaseTrxDetails.filter(and_(*conditions)).all()   
        
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
    purchasetrxheader.supplier_id = raw_data['supplier_id']
    purchasetrxheader.amount = raw_data['amount']
    purchasetrxheader.last_updated_by = raw_data['last_updated_by']
    
    purchasetrxLines = []
    
    for purchase_trx_line in raw_data['purchase_trx_lines']:
        if 'transaction_line_id' in purchase_trx_line.keys():
            for trx_line in purchasetrxheader.purchase_trx_lines:
                if purchase_trx_line["transaction_line_id"] == trx_line.transaction_line_id:
                    trx_line.item_id = purchase_trx_line['item_id']
                    trx_line.line_number = purchase_trx_line['line_number']
                    trx_line.item_description = purchase_trx_line['item_description']
                    trx_line.booking_unit_price = purchase_trx_line['booking_unit_price']
                    trx_line.booking_quantity = purchase_trx_line['booking_quantity']
                    trx_line.unit_of_measure = purchase_trx_line['unit_of_measure']
                    trx_line.discount = purchase_trx_line['discount']
                    trx_line.created_by = purchase_trx_line['created_by']
                    trx_line.last_updated_by = purchase_trx_line['last_updated_by']   
                    break
        else:
            purchasetrxLine = PurchaseTrxLines()
            purchasetrxLine.item_id = purchase_trx_line['item_id']
            purchasetrxLine.line_number = purchase_trx_line['line_number']
            purchasetrxLine.item_description = purchase_trx_line['item_description']
            purchasetrxLine.booking_unit_price = purchase_trx_line['booking_unit_price']
            purchasetrxLine.booking_quantity = purchase_trx_line['booking_quantity']
            purchasetrxLine.unit_of_measure = purchase_trx_line['unit_of_measure']
            purchasetrxLine.discount = purchase_trx_line['discount']
            purchasetrxLine.created_by = purchase_trx_line['created_by']
            purchasetrxLine.last_updated_by = purchase_trx_line['last_updated_by']   
            purchasetrxLines.append(purchasetrxLine)
    
    if len(purchasetrxLines) > 0:
        purchasetrxheader.purchase_trx_lines.extend(purchasetrxLines)
            

@db_transaction
def get_purchase_trx_detail(purchase_trx_number,session):
    purchasetrxheader = session.query(PurchaseTrxHeader).filter_by(purchase_trx_number=purchase_trx_number).first()
    result = dict(purchasetrxheader.__dict__)
    result.pop('_sa_instance_state')
    line_dicts = []
    for line in purchasetrxheader.purchase_trx_lines:
        line_dict = dict(line.__dict__)
        line_dict.pop('_sa_instance_state')
        line_dicts.append(line_dict)
    result['purchase_trx_lines'] = line_dicts
    return result
                
    