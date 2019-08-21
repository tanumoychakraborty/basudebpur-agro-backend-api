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
from sqlalchemy import func

@db_transaction
def create_challan(raw_data, session):
    challanheader = ReceiptHeader()
    Challan_number = session.query(func.apps.generate_challan_number()).first()
    challanheader.challan_number = Challan_number[0]
    challanheader.created_by = raw_data['created_by']
    #challanheader.challan_date= raw_data['challan_date']
    challanheader.last_updated_by = raw_data['last_updated_by']
    challanheader.source_transaction_header_id = raw_data['source_transaction_header_id']
    challanheader.source_transaction_type = raw_data['source_transaction_type']
    #challanheader.vehicle_number = raw_data['vehicle_number']
    x = session.add(challanheader)
    
    #Challan_number = dict(Challan_number.__dict__)
    #Challan_number.pop('_sa_instance_state')
    
    challan =  dict(challanheader.__dict__)
    challan.pop('_sa_instance_state')
    return challan
    

@db_transaction
def update_receipt_data(raw_data, session):
    challan_number = raw_data['challan_number']
    challanheader = session.query(ReceiptHeader).filter_by(challan_number=challan_number).first()
    if challanheader is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="Challan number does not exist")
    
    #receipt_number = session.query(func.apps.generate_receipt_number()).first()
    #challanheader.receipt_number = receipt_number[0]
    #challanheader.receipt_date = raw_data['receipt_date']
    challanheader.challan_date = raw_data['challan_date']
    #challanheader.source_transaction_header_id = raw_data['source_transaction_header_id']
    #challanheader.source_transaction_type = raw_data['source_transaction_type']
    challanheader.vehicle_number = raw_data['vehicle_number']
    challanheader.last_updated_by = get_user_id_by_user_name(raw_data['last_updated_by'])
    
    challanLines = []
    
    for challan_line in raw_data['receipt_lines']:
        if 'receipt_line_id' in challan_line.keys():
            for challanLine in challanheader.receipt_lines:
                if challan_line["receipt_line_id"] == challanLine.receipt_line_id:
                    challanLine.item_id = challan_line['item_id']
                    challanLine.line_number = challan_line['line_number']
                    #challanLine.load_unload_number = challan_line['load_unload_number']
                    challanLine.load_unload_area = challan_line['load_unload_area']
                    challanLine.weighing_number = challan_line['weighing_number']
                    challanLine.receipt_line_status = challan_line['receipt_line_status']
                    challanLine.quantity = challan_line['quantity']
                    challanLine.unit_price = challan_line['unit_price']
                    challanLine.unit_of_measure = challan_line['unit_of_measure']
                    challanLine.discount = challan_line['discount']
                    challanLine.last_updated_by = get_user_id_by_user_name(challan_line['last_updated_by'])   
                    break
        else:
                    chalanLine = ReceiptLines()
                    chalanLine.item_id = challan_line['item_id']
                    chalanLine.line_number = challan_line['line_number']
                    #chalanLine.load_unload_number = challan_line['load_unload_number']
                    chalanLine.load_unload_area = challan_line['load_unload_area']
                    chalanLine.weighing_number = challan_line['weighing_number']
                    chalanLine.receipt_line_status = challan_line['receipt_line_status']
                    chalanLine.quantity = challan_line['quantity']
                    chalanLine.unit_price = challan_line['unit_price']
                    chalanLine.unit_of_measure = challan_line['unit_of_measure']
                    chalanLine.discount = challan_line['discount']
                    chalanLine.last_updated_by = get_user_id_by_user_name(challan_line['last_updated_by'])
                    chalanLine.created_by = get_user_id_by_user_name(challan_line['last_updated_by'])
                    challanLines.append(chalanLine)
    
    if len(challanLines) > 0:
        challanheader.receipt_lines.extend(challanLines)
        

@db_transaction
def get_receipt_details(params,page, page_size,session):
    resultL = []
    if params is None:
        receiptDetails = session.query(ReceiptHeader.receipt_header_id,ReceiptHeader.receipt_number,ReceiptHeader.challan_number,
                                           ReceiptHeader.receipt_date,ReceiptHeader.challan_date,ReceiptHeader.vehicle_number).limit(500).all()
        if page_size:
            receiptDetails = receiptDetails.limit(page_size)
        if page: 
            receiptDetails = receiptDetails.offset(page*page_size)
    else:
        receipt_header_id = params.get('receipt_header_id',None)
        receipt_number = params.get('receipt_number',None)
        challan_number = params.get('challan_number',None)
        receipt_date = params.get('receipt_date',None)
        challan_date = params.get('challan_date',None)
        from_receipt_date = params.get('from_receipt_date',None)
        to_receipt_date = params.get('to_receipt_date',None)
        source_transaction_header_id = params.get('source_transaction_header_id',None)
        source_transaction_type = params.get('source_transaction_type',None)
        
        receiptDetails = session.query(ReceiptHeader.receipt_header_id,ReceiptHeader.receipt_number,ReceiptHeader.challan_number,
                                           ReceiptHeader.receipt_date,ReceiptHeader.challan_date, ReceiptHeader.vehicle_number)
        conditions = []
        if receipt_header_id:
            conditions.append(ReceiptHeader.receipt_header_id == receipt_header_id)
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
        if source_transaction_header_id:
            conditions.append(ReceiptHeader.source_transaction_header_id == source_transaction_header_id)
        if source_transaction_type:
            conditions.append(ReceiptHeader.source_transaction_type == source_transaction_type)          
                
            
                
        receiptDetails = receiptDetails.filter(and_(*conditions)).all()   
        
        if page_size:
            receiptDetails = receiptDetails.limit(page_size)
        if page: 
            receiptDetails = receiptDetails.offset(page*page_size) 
                  
    for receiptDetail in receiptDetails:
        dict ={ }
        dict['receipt_header_id'] = receiptDetail[0]
        dict['receipt_number'] = receiptDetail[1]
        dict['challan_number'] = receiptDetail[2]
        dict['receipt_date'] = receiptDetail[3]
        dict['challan_date'] = receiptDetail[4]
        dict['vehicle_number'] = receiptDetail[5]
        
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

@db_transaction
def get_receipt_detail_by_challan_number(challan_number,session):
    receiptheader = session.query(ReceiptHeader).filter_by(challan_number=challan_number).first()
    result = dict(receiptheader.__dict__)
    result.pop('_sa_instance_state')
    line_dicts = []
    for line in receiptheader.receipt_lines:
        line_dict = dict(line.__dict__)
        line_dict.pop('_sa_instance_state')
        line_dicts.append(line_dict)
    result['receipt_lines'] = line_dicts
    return result



