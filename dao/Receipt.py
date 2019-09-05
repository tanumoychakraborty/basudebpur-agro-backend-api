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
import datetime

@db_transaction
def create_challan(raw_data, session):
    challanheader = ReceiptHeader()
    Challan_number = session.query(func.apps.generate_challan_number()).first()
    challanheader.challan_number = Challan_number[0]
    challanheader.created_by = raw_data['created_by']
    challanheader.challan_date = datetime.datetime.utcnow()
    challanheader.last_updated_by = raw_data['last_updated_by']
    challanheader.source_transaction_header_id = raw_data['source_transaction_header_id']
    challanheader.source_transaction_type = raw_data['source_transaction_type']    
    challanheader.receipt_header_status = 'OPEN'
    session.add(challanheader)
    
    challan =  dict(challanheader.__dict__)
    challan.pop('_sa_instance_state')
    return challan
    

@db_transaction
def update_receipt_data(raw_data, session):
    challan_number = raw_data['challan_number']
    challanheader = session.query(ReceiptHeader).filter_by(challan_number=challan_number).first()
    if challanheader is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="Challan number does not exist")
    if 'vehicle_number' in raw_data.keys():
        challanheader.vehicle_number = raw_data['vehicle_number']
    if 'bata' in raw_data.keys():    
        challanheader.bata = raw_data['bata']    
    if 'receipt_header_status' in raw_data.keys():
        challanheader.receipt_header_status = raw_data['receipt_header_status']
    if 'net_weight' in raw_data.keys():
        challanheader.net_weight = raw_data['net_weight']
    if 'average_weight' in raw_data.keys():
        challanheader.average_weight = raw_data['average_weight']
    if 'unit_of_measure' in raw_data.keys():
        challanheader.unit_of_measure = raw_data['unit_of_measure']
    if 'total_bags' in raw_data.keys():
        challanheader.total_bags = raw_data['total_bags']
    challanheader.last_updated_by = get_user_id_by_user_name(raw_data['last_updated_by'])
    
    challanLines = []
    is_receipt_complete = False
    if 'receipt_lines' in raw_data.keys():
        for challan_line in raw_data['receipt_lines']:
            if 'receipt_line_id' in challan_line.keys():
                for challanLine in challanheader.receipt_lines:
                    if challan_line["receipt_line_id"] == challanLine.receipt_line_id:
                        if 'item_id' in challan_line.keys():
                            challanLine.item_id = challan_line['item_id']
                        if 'description' in challan_line.keys():
                            challanLine.description = challan_line['description']
                        if 'line_number' in challan_line.keys():
                            challanLine.line_number = challan_line['line_number']
                        if 'load_unload_number' in challan_line.keys():
                            challanLine.load_unload_number = challan_line['load_unload_number']
                        if 'load_unload_area' in challan_line.keys():
                            challanLine.load_unload_area = challan_line['load_unload_area']
                        if 'weighing_number' in challan_line.keys():
                            challanLine.weighing_number = challan_line['weighing_number']
                        if 'receipt_line_status' in challan_line.keys():
                            challanLine.receipt_line_status = challan_line['receipt_line_status']
                        if 'quantity' in challan_line.keys():
                            challanLine.quantity = challan_line['quantity']
                        if 'number_of_bags' in challan_line.keys():
                            challanLine.number_of_bags = challan_line['number_of_bags']
                        if 'unit_price' in challan_line.keys():
                            challanLine.unit_price = challan_line['unit_price']
                        if 'unit_of_measure' in challan_line.keys():
                            challanLine.unit_of_measure = challan_line['unit_of_measure']
                        if 'discount' in challan_line.keys():
                            challanLine.discount = challan_line['discount']
                        if 'last_updated_by' in challan_line.keys():
                            challanLine.last_updated_by = get_user_id_by_user_name(challan_line['last_updated_by'])   
                        if challan_line['receipt_line_status'] == 'COMPLETE':
                            is_receipt_complete = is_receipt_complete or True
                        else:
                            is_receipt_complete = is_receipt_complete and False
                            
                        break
            else:
                        challanLine = ReceiptLines()
                        if 'item_id' in challan_line.keys():
                            challanLine.item_id = challan_line['item_id']
                        if 'description' in challan_line.keys():
                            challanLine.description = challan_line['description']
                        if 'line_number' in challan_line.keys():
                            challanLine.line_number = challan_line['line_number']
                        if 'load_unload_number' in challan_line.keys():
                            challanLine.load_unload_number = challan_line['load_unload_number']
                        if 'load_unload_area' in challan_line.keys():
                            challanLine.load_unload_area = challan_line['load_unload_area']
                        if 'weighing_number' in challan_line.keys():
                            challanLine.weighing_number = challan_line['weighing_number']
                        if 'receipt_line_status' in challan_line.keys():
                            challanLine.receipt_line_status = challan_line['receipt_line_status']
                        if 'quantity' in challan_line.keys():
                            challanLine.quantity = challan_line['quantity']
                        if 'number_of_bags' in challan_line.keys():
                            challanLine.number_of_bags = challan_line['number_of_bags']
                        if 'unit_price' in challan_line.keys():
                            challanLine.unit_price = challan_line['unit_price']
                        if 'unit_of_measure' in challan_line.keys():
                            challanLine.unit_of_measure = challan_line['unit_of_measure']
                        if 'discount' in challan_line.keys():
                            challanLine.discount = challan_line['discount']
                        if 'last_updated_by' in challan_line.keys():
                            challanLine.last_updated_by = get_user_id_by_user_name(challan_line['last_updated_by'])
                            challanLine.created_by = get_user_id_by_user_name(challan_line['last_updated_by'])
                        challanLines.append(challanLine)
                        is_receipt_complete = is_receipt_complete and False
                        
        
    
        if len(challanLines) > 0:
            challanheader.receipt_lines.extend(challanLines)
        else:
            if is_receipt_complete:
                challanheader.receipt_header_status = 'COMPLETE'
                challanheader.receipt_date = datetime.datetime.utcnow()
        

@db_transaction
def get_receipt_details(params,page, page_size,session):
    resultL = []
    if params is None:
        receiptDetails = session.query(ReceiptHeader.receipt_header_id, ReceiptHeader.receipt_number, ReceiptHeader.challan_number, ReceiptHeader.receipt_date, ReceiptHeader.challan_date, 
                                           ReceiptHeader.vehicle_number, ReceiptHeader.receipt_header_status, ReceiptHeader.bata, ReceiptHeader.source_transaction_header_id, ReceiptHeader.net_weight, 
                                           ReceiptHeader.average_weight, ReceiptHeader.unit_of_measure, ReceiptHeader.total_bags).limit(500).all()
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
        from_challan_date = params.get('from_challan_date',None)
        to_challan_date = params.get('to_challan_date',None)
        source_transaction_header_id = params.get('source_transaction_header_id',None)
        source_transaction_type = params.get('source_transaction_type',None)
        receipt_header_status = params.get('receipt_header_status',None)
        
        receiptDetails = session.query(ReceiptHeader.receipt_header_id, ReceiptHeader.receipt_number, ReceiptHeader.challan_number, ReceiptHeader.receipt_date, ReceiptHeader.challan_date, 
                                           ReceiptHeader.vehicle_number, ReceiptHeader.receipt_header_status, ReceiptHeader.bata, ReceiptHeader.source_transaction_header_id,  
                                           ReceiptHeader.net_weight, ReceiptHeader.average_weight, ReceiptHeader.unit_of_measure, ReceiptHeader.total_bags)
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
            conditions.append(ReceiptHeader.receipt_date >= from_receipt_date)
        if to_receipt_date:
            conditions.append(ReceiptHeader.receipt_date <= to_receipt_date) 
        if from_challan_date:
            conditions.append(ReceiptHeader.challan_date >= from_challan_date)
        if to_challan_date:
            conditions.append(ReceiptHeader.challan_date <= to_challan_date)      
        if source_transaction_header_id:
            conditions.append(ReceiptHeader.source_transaction_header_id == source_transaction_header_id)
        if source_transaction_type:
            conditions.append(ReceiptHeader.source_transaction_type == source_transaction_type) 
        if receipt_header_status:
            conditions.append(ReceiptHeader.receipt_header_status == receipt_header_status)          
                
            
                
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
        dict['receipt_header_status'] = receiptDetail[6]
        dict['bata'] = receiptDetail[7]
        dict['source_transaction_header_id'] = receiptDetail[8]
        dict['net_weight'] = receiptDetail[9]
        dict['average_weight'] = receiptDetail[10]
        dict['unit_of_measure'] = receiptDetail[11]
        dict['total_bags'] = receiptDetail[12]
        
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



