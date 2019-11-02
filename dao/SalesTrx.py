'''
Created on 29-Aug-2019

@author: duttasudip89
'''
from model.SalesTrxHeader import SalesTrxHeader
from model.SalesTrxLines import SalesTrxLines
from model.CustomerMasterHeader import CustomerMasterHeader
from util.db_helper import db_transaction
from sqlalchemy.sql.expression import and_
from falcon.http_error import HTTPError
from falcon import status_codes
from sqlalchemy import func
from dao.Users import get_user_id_by_user_name

@db_transaction
def create_sales_trx(raw_data, session):
    salestrxheader = SalesTrxHeader()
    so_number = session.query(func.apps.generate_so_number()).first()
    salestrxheader.sales_trx_number = so_number[0]
    if 'transaction_date' in raw_data.keys():
        salestrxheader.transaction_date = raw_data['transaction_date']
    if 'order_status' in raw_data.keys():
        salestrxheader.order_status = raw_data['order_status']
    if 'sales_rep_id' in raw_data.keys():
        salestrxheader.sales_rep_id = raw_data['sales_rep_id']
    if 'customer_id' in raw_data.keys():
        salestrxheader.customer_id = raw_data['customer_id']
    if 'created_by' in raw_data.keys():
        salestrxheader.created_by = raw_data['created_by']
    if 'last_updated_by' in raw_data.keys():
        salestrxheader.last_updated_by = raw_data['last_updated_by']
        
    salestrxLines = []
    if 'sales_trx_lines' in raw_data.keys():
        for sales_trx_line in raw_data['sales_trx_lines']:
            salestrxLine = SalesTrxLines()
            if 'item_id' in sales_trx_line.keys():
                salestrxLine.item_id = sales_trx_line['item_id']
            if 'line_number' in sales_trx_line.keys():
                salestrxLine.line_number = sales_trx_line['line_number']
            if 'booking_unit_price' in sales_trx_line.keys():
                salestrxLine.booking_unit_price = sales_trx_line['booking_unit_price']
            if 'booking_quantity' in sales_trx_line.keys():
                salestrxLine.booking_quantity = sales_trx_line['booking_quantity']
            if 'unit_of_measure' in sales_trx_line.keys():
                salestrxLine.unit_of_measure = sales_trx_line['unit_of_measure']
            if 'created_by' in sales_trx_line.keys():
                salestrxLine.created_by = sales_trx_line['created_by']
            if 'last_updated_by' in sales_trx_line.keys():
                salestrxLine.last_updated_by = sales_trx_line['last_updated_by']   
            salestrxLines.append(salestrxLine)
            
    salestrxheader.sales_trx_lines = salestrxLines
     
    session.add(salestrxheader)
    
    return salestrxheader

@db_transaction
def get_sales_transaction_details(params,page, page_size,session):
    resultL = []
    if params is None:
        salesTrxDetails = session.query(SalesTrxHeader.sales_trx_number,SalesTrxHeader.transaction_date,
                                           CustomerMasterHeader.customer_name,SalesTrxHeader.order_status).join(CustomerMasterHeader,SalesTrxHeader.customer_id==CustomerMasterHeader.customer_id).limit(500).all()
        if page_size:
            salesTrxDetails = salesTrxDetails.limit(page_size)
        if page: 
            salesTrxDetails = salesTrxDetails.offset(page*page_size)
    else:
        sales_trx_number = params.get('sales_trx_number',None)
        customer_id = params.get('customer_id',None)
        transaction_date = params.get('transaction_date',None)
        sales_rep_id = params.get('sales_rep_id',None)
        from_creation_date = params.get('from_creation_date',None)
        to_creation_date = params.get('to_creation_date',None)
        order_status = params.get('order_status',None)
        
        salesTrxDetails = session.query(SalesTrxHeader.sales_trx_number,SalesTrxHeader.transaction_date,
                                           CustomerMasterHeader.customer_name,SalesTrxHeader.order_status).join(CustomerMasterHeader,SalesTrxHeader.customer_id==CustomerMasterHeader.customer_id).order_by(SalesTrxHeader.sales_trx_number)
         
        conditions = []
        if sales_trx_number:
            conditions.append(SalesTrxHeader.sales_trx_number == sales_trx_number)
        if customer_id:
            conditions.append(SalesTrxHeader.customer_id == customer_id)
        if transaction_date:
            conditions.append(SalesTrxHeader.transaction_date == transaction_date)
        if sales_rep_id:
            conditions.append(SalesTrxHeader.sales_rep_id == sales_rep_id)
        if from_creation_date:
            conditions.append(SalesTrxHeader.creation_date >= from_creation_date)
        if to_creation_date:
            conditions.append(SalesTrxHeader.creation_date <= to_creation_date)    
        if order_status:
            conditions.append(SalesTrxHeader.order_status == order_status)            
                
            
                
        salesTrxDetails = salesTrxDetails.filter(and_(*conditions)).all()   
        
        if page_size:
            salesTrxDetails = salesTrxDetails.limit(page_size)
        if page: 
            salesTrxDetails = salesTrxDetails.offset(page*page_size) 
                  
    for salesTrxDetail in salesTrxDetails:
        dict ={ }
        dict['sales_trx_number'] = salesTrxDetail[0]
        dict['transaction_date'] = salesTrxDetail[1]
        dict['customer_name'] = salesTrxDetail[2]
        dict['order_status'] = salesTrxDetail[3]
        
        resultL.append(dict)    
            
    return resultL



@db_transaction
def update_sales_trx(raw_data,session):
    sales_trx_number = raw_data['sales_trx_number']
    salestrxheader = session.query(SalesTrxHeader).filter_by(sales_trx_number=sales_trx_number).first()
    if salestrxheader is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="Sales Transaction number does not exist")
    if 'transaction_date' in raw_data.keys():
        salestrxheader.transaction_date = raw_data['transaction_date']
    if 'order_status' in raw_data.keys():    
        salestrxheader.order_status = raw_data['order_status']
    if 'sales_rep_id' in raw_data.keys():     
        salestrxheader.sales_rep_id = raw_data['sales_rep_id']
    if 'customer_id' in raw_data.keys():    
        salestrxheader.customer_id = raw_data['customer_id']
    if 'last_updated_by' in raw_data.keys():    
        salestrxheader.last_updated_by = get_user_id_by_user_name(raw_data['last_updated_by']) 
    
    salestrxLines = []
    
    if 'sales_trx_lines' in raw_data.keys():
        for sales_trx_line in raw_data['sales_trx_lines']:
            if 'transaction_line_id' in sales_trx_line.keys():
                for trx_line in salestrxheader.sales_trx_lines:
                    if sales_trx_line["transaction_line_id"] == trx_line.transaction_line_id:
                        if 'item_id' in sales_trx_line:
                            trx_line.item_id = sales_trx_line['item_id']
                        #trx_line.line_number = sales_trx_line['line_number']
                        if 'booking_unit_price' in sales_trx_line:
                            trx_line.booking_unit_price = sales_trx_line['booking_unit_price']
                        if 'booking_quantity' in sales_trx_line:
                            trx_line.booking_quantity = sales_trx_line['booking_quantity']
                        if 'unit_of_measure' in sales_trx_line:
                            trx_line.unit_of_measure = sales_trx_line['unit_of_measure']
                        #trx_line.created_by = sales_trx_line['created_by']
                        trx_line.last_updated_by = get_user_id_by_user_name(sales_trx_line['last_updated_by'])    
                        break
            else:
                salestrxLine = SalesTrxLines()
                if 'item_id' in sales_trx_line:
                    salestrxLine.item_id = sales_trx_line['item_id']
                if 'line_number' in sales_trx_line:
                    salestrxLine.line_number = sales_trx_line['line_number']
                if 'booking_unit_price' in sales_trx_line:
                    salestrxLine.booking_unit_price = sales_trx_line['booking_unit_price']
                if 'booking_quantity' in sales_trx_line:
                    salestrxLine.booking_quantity = sales_trx_line['booking_quantity']
                if 'unit_of_measure' in sales_trx_line:
                    salestrxLine.unit_of_measure = sales_trx_line['unit_of_measure']
                salestrxLine.created_by = get_user_id_by_user_name(sales_trx_line['created_by'])
                salestrxLine.last_updated_by = get_user_id_by_user_name(sales_trx_line['last_updated_by'])  
                salestrxLines.append(salestrxLine)
    
    if len(salestrxLines) > 0:
        salestrxheader.sales_trx_lines.extend(salestrxLines)
            

@db_transaction
def get_sales_trx_detail(sales_trx_number,session):
    salestrxheader = session.query(SalesTrxHeader).filter_by(sales_trx_number=sales_trx_number).first()
    result = dict(salestrxheader.__dict__)
    result.pop('_sa_instance_state')
    line_dicts = []
    for line in salestrxheader.sales_trx_lines:
        line_dict = dict(line.__dict__)
        line_dict.pop('_sa_instance_state')
        line_dict['item_id'] = str(line_dict['item_id'])
        line_dicts.append(line_dict)
    result['sales_trx_lines'] = line_dicts
    return result
