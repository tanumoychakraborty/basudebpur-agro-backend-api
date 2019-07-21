'''
Created on 07-Jul-2019

@author: duttasudip89
'''

from model.ReceiptHeader import ReceiptHeader
from model.ReceiptLines import ReceiptLines
from dao.Users import get_user_id_by_user_name
from util.db_helper import db_transaction
from sqlalchemy.sql.expression import and_
from falcon.http_error import HTTPError
from falcon import status_codes

@db_transaction
def create_receipt(raw_data, session):
    receiptheader = ReceiptHeader()
    receiptheader.receipt_number = raw_data['receipt_number']
    receiptheader.challan_number = raw_data['challan_number']
    receiptheader.receipt_date = raw_data['receipt_date']
    receiptheader.challan_date = raw_data['challan_date']
    receiptheader.source_transaction_header_id = raw_data['source_transaction_header_id']
    receiptheader.source_transaction_type = raw_data['source_transaction_type']
    receiptheader.vehicle_number = raw_data['vehicle_number']
    receiptheader.created_by = raw_data['created_by']
    receiptheader.last_updated_by = raw_data['last_updated_by']
        
    receiptLines = []
    for receipt_line in raw_data['receipt_lines']:
        receiptLine = ReceiptLines()
        receiptLine.item_id = receipt_line['item_id']
        receiptLine.line_number = receipt_line['line_number']
        receiptLine.load_unload_number = receipt_line['load_unload_number']
        receiptLine.load_unload_area = receipt_line['load_unload_area']
        receiptLine.weighting_number = receipt_line['weighting_number']
        receiptLine.receipt_line_status = receipt_line['receipt_line_status']
        receiptLine.quantity = receipt_line['quantity']
        receiptLine.unit_price = receipt_line['unit_price']
        receiptLine.line_number = receipt_line['line_number']
        receiptLine.unit_of_measure = receipt_line['unit_of_measure']
        receiptLine.discount = receipt_line['discount']
        receiptLine.created_by = receipt_line['created_by']
        receiptLine.last_updated_by = receipt_line['last_updated_by']   
        receiptLines.append(receiptLine)
            
    receiptheader.receipt_lines = receiptLines
     
    session.add(receiptheader)
    
    return receiptheader

@db_transaction
def update_receipt(raw_data,session):
    receipt_number = raw_data['receipt_number']
    receiptheader = session.query(ReceiptHeader).filter_by(receipt_number=receipt_number).first()
    if receiptheader is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="Receipt number does not exist")
    receiptheader.challan_number = raw_data['challan_number']
    receiptheader.receipt_date = raw_data['receipt_date']
    receiptheader.challan_date = raw_data['challan_date']
    receiptheader.source_transaction_header_id = raw_data['source_transaction_header_id']
    receiptheader.source_transaction_type = raw_data['source_transaction_type']
    receiptheader.vehicle_number = raw_data['vehicle_number']
    receiptheader.last_updated_by = get_user_id_by_user_name(raw_data['last_updated_by'])
    
    receiptLines = []
    
    for receipt_line in raw_data['receipt_lines']:
        if 'receipt_line_id' in receipt_line.keys():
            for receiptLine in receiptheader.receipt_lines:
                if receipt_line["receipt_line_id"] == receiptLine.receipt_line_id:
                    receiptLine.item_id = receipt_line['item_id']
                    receiptLine.line_number = receipt_line['line_number']
                    receiptLine.load_unload_number = receipt_line['load_unload_number']
                    receiptLine.load_unload_area = receipt_line['load_unload_area']
                    receiptLine.weighting_number = receipt_line['weighting_number']
                    receiptLine.receipt_line_status = receipt_line['receipt_line_status']
                    receiptLine.quantity = receipt_line['quantity']
                    receiptLine.unit_price = receipt_line['unit_price']
                    receiptLine.line_number = receipt_line['line_number']
                    receiptLine.unit_of_measure = receipt_line['unit_of_measure']
                    receiptLine.discount = receipt_line['discount']
                    receiptLine.last_updated_by = get_user_id_by_user_name(receipt_line['last_updated_by'])   
                    break
        else:
                    receiptLine = ReceiptLines()
                    receiptLine.item_id = receipt_line['item_id']
                    receiptLine.line_number = receipt_line['line_number']
                    receiptLine.load_unload_number = receipt_line['load_unload_number']
                    receiptLine.load_unload_area = receipt_line['load_unload_area']
                    receiptLine.weighting_number = receipt_line['weighting_number']
                    receiptLine.receipt_line_status = receipt_line['receipt_line_status']
                    receiptLine.quantity = receipt_line['quantity']
                    receiptLine.unit_price = receipt_line['unit_price']
                    receiptLine.line_number = receipt_line['line_number']
                    receiptLine.unit_of_measure = receipt_line['unit_of_measure']
                    receiptLine.discount = receipt_line['discount']
                    receiptLine.last_updated_by = get_user_id_by_user_name(receipt_line['last_updated_by'])
                    receiptLine.created_by = get_user_id_by_user_name(receipt_line['last_updated_by'])
                    receiptLines.append(receiptLine)
    
    if len(receiptLines) > 0:
        receiptheader.receipt_lines.extend(receiptLines)
        

@db_transaction
def get_receipt_details(params,page, page_size,session):
    resultL = []
    if params is None:
        receiptDetails = session.query(ReceiptHeader.receipt_number,ReceiptHeader.challan_number,
                                           ReceiptHeader.receipt_date,ReceiptHeader.challan_date).limit(500).all()
        if page_size:
            receiptDetails = receiptDetails.limit(page_size)
        if page: 
            receiptDetails = receiptDetails.offset(page*page_size)
    else:
        receipt_number = params.get('receipt_number',None)
        challan_number = params.get('challan_number',None)
        receipt_date = params.get('receipt_date',None)
        challan_date = params.get('challan_date',None)
        from_receipt_date = params.get('from_receipt_date',None)
        to_receipt_date = params.get('to_receipt_date',None)
        
        receiptDetails = session.query(ReceiptHeader.receipt_number,ReceiptHeader.challan_number,
                                           ReceiptHeader.receipt_date,ReceiptHeader.challan_date)
        conditions = []
        if receipt_number:
            conditions.append(ReceiptHeader.receipt_number == receipt_number)
        if challan_number:
            conditions.append(ReceiptHeader.challan_number == challan_number)
        if receipt_date:
            conditions.append(ReceiptHeader.receipt_date == receipt_date)
        if challan_date:
            conditions.append(ReceiptHeader.challan_date == challan_date)
        if from_receipt_date:
            conditions.append(ReceiptHeader.creation_date >= from_receipt_date)
        if to_receipt_date:
            conditions.append(ReceiptHeader.creation_date <= to_receipt_date)          
                
            
                
        receiptDetails = receiptDetails.filter(and_(*conditions)).all()   
        
        if page_size:
            receiptDetails = receiptDetails.limit(page_size)
        if page: 
            receiptDetails = receiptDetails.offset(page*page_size) 
                  
    for receiptDetail in receiptDetails:
        dict ={ }
        dict['receipt_number'] = receiptDetail[0]
        dict['challan_number'] = receiptDetail[1]
        dict['receipt_date'] = receiptDetail[2]
        dict['challan_date'] = receiptDetail[3]
        
        resultL.append(dict)    
            
    return resultL




            

@db_transaction
def get_receipt_detail(receipt_number,session):
    receiptheader = session.query(ReceiptHeader).filter_by(receipt_number=receipt_number).first()
    result = dict(receiptheader.__dict__)
    result.pop('_sa_instance_state')
    line_dicts = []
    for line in receiptheader.receipt_lines:
        line_dict = dict(line.__dict__)
        line_dict.pop('_sa_instance_state')
        line_dicts.append(line_dict)
    result['receipt_lines'] = line_dicts
    return result
