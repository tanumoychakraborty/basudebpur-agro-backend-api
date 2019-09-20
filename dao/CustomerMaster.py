'''
Created on 06-Apr-2019

@author: duttasudip89
'''

from model.CustomerMasterHeader import CustomerMasterHeader
from model.CustomerMasterSites import CustomerMasterSites
from util.db_helper import db_transaction
from sqlalchemy.sql.expression import and_
from falcon.http_error import HTTPError
from falcon import status_codes

@db_transaction
def get_customer_details(session):
    resultL = []
    
    customerDetails = session.query(CustomerMasterHeader).all()
                  
    for customerDetail in customerDetails:
        dict = { }
        dict['customer_id'] = customerDetail.customer_id
        dict['customer_name'] = customerDetail.customer_name
        dict['description'] = customerDetail.description
        dict['customer_code'] = customerDetail.customer_code
        dict['customer_type'] = customerDetail.customer_type
        resultL.append(dict) 
    return resultL

@db_transaction
def search_customer_details(params,page, page_size,session):
        resultL = []
        customer_code = params.get('customer_code',None)
        customer_name = params.get('customer_name',None)
        customer_type = params.get('customer_type',None)
        
        customerDetails = session.query(CustomerMasterHeader.customer_code,CustomerMasterHeader.customer_name,
                                           CustomerMasterHeader.description,CustomerMasterHeader.customer_type,CustomerMasterHeader.enabled_flag)
         
        conditions = []
        if customer_code:
            conditions.append(CustomerMasterHeader.customer_code == customer_code)
        if customer_name:
            conditions.append(CustomerMasterHeader.customer_name == customer_name)
        if customer_type:
            conditions.append(CustomerMasterHeader.customer_type == customer_type)
            
                
        customerDetails = customerDetails.filter(and_(*conditions)).all()   
        
        if page_size:
            customerDetails = customerDetails.limit(page_size)
        if page: 
            customerDetails = customerDetails.offset(page*page_size) 
                  
        for customerDetail in customerDetails:
            dict ={ }
            dict['customer_code'] = customerDetail[0]
            dict['customer_name'] = customerDetail[1]
            dict['description'] = customerDetail[2]
            dict['customer_type'] = customerDetail[3]
            dict['enabled_flag'] = customerDetail[4]
            
            resultL.append(dict)    
                
        return resultL 
    

@db_transaction
def create_customer(raw_data, session):
    customerMasterHeader = CustomerMasterHeader()
    if 'customer_code' in raw_data.keys():
        customerMasterHeader.customer_code = raw_data['customer_code']
    if 'customer_name' in raw_data.keys():
        customerMasterHeader.customer_name = raw_data['customer_name']
    if 'description' in raw_data.keys():
        customerMasterHeader.description = raw_data['description']
    if 'customer_type' in raw_data.keys():
        customerMasterHeader.customer_type = raw_data['customer_type']
    if 'remarks' in raw_data.keys():
        customerMasterHeader.remarks = raw_data['remarks']
    if 'enabled_flag' in raw_data.keys():
        customerMasterHeader.enabled_flag = raw_data['enabled_flag']
    if 'effective_from' in raw_data.keys():
        customerMasterHeader.effective_from = raw_data['effective_from']
    if 'effective_to' in raw_data.keys():
        customerMasterHeader.effective_to = raw_data['effective_to']
    if 'created_by' in raw_data.keys():
        customerMasterHeader.created_by = raw_data['created_by']
    if 'last_updated_by' in raw_data.keys():
        customerMasterHeader.last_updated_by = raw_data['last_updated_by'] 
        
    CustomerMasterSitesList = []
    for customer_master_Site in raw_data['customer_master_sites']:
        CustomerMasterSite = CustomerMasterSites()
        if 'customer_site_code' in customer_master_Site.keys():
            CustomerMasterSite.customer_site_code = customer_master_Site['customer_site_code']
        if 'customer_address' in customer_master_Site.keys():
            CustomerMasterSite.customer_site_address = customer_master_Site['customer_address']
        if 'phone_number1' in customer_master_Site.keys():
            CustomerMasterSite.phone_number1 = customer_master_Site['phone_number1']
        if 'phone_number2' in customer_master_Site.keys():
            CustomerMasterSite.phone_number2 = customer_master_Site['phone_number2']
        if 'email' in customer_master_Site.keys():
            CustomerMasterSite.email = customer_master_Site['email']
        '''
                other fields also need to include
        '''
        if 'effective_from' in customer_master_Site.keys():
            CustomerMasterSite.effective_from = raw_data['effective_from']
        if 'effective_to' in customer_master_Site.keys():
            CustomerMasterSite.effective_to = raw_data['effective_to']
        if 'created_by' in customer_master_Site.keys():
            CustomerMasterSite.created_by = customer_master_Site['created_by']
        if 'last_updated_by' in customer_master_Site.keys():
            CustomerMasterSite.last_updated_by = customer_master_Site['last_updated_by']   
        CustomerMasterSitesList.append(CustomerMasterSite)
            
    customerMasterHeader.sites = CustomerMasterSitesList
     
    session.add(customerMasterHeader)
    
    return CustomerMasterHeader


@db_transaction
def update_customer(raw_data,session):
    customer_code = raw_data['customer_code']
    
    customerMasterHeader = session.query(CustomerMasterHeader).filter_by(customer_code=customer_code).first()
    if customerMasterHeader is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="Customer does not exist")
    
    if 'customer_name' in raw_data.keys():
        customerMasterHeader.customer_name = raw_data['customer_name']
    if 'description' in raw_data.keys():
        customerMasterHeader.description = raw_data['description']
    if 'customer_type' in raw_data.keys():
        customerMasterHeader.customer_type = raw_data['customer_type']
    if 'remarks' in raw_data.keys():
        customerMasterHeader.remarks = raw_data['remarks']
    if 'enabled_flag' in raw_data.keys():
        customerMasterHeader.enabled_flag = raw_data['enabled_flag']
    if 'effective_from' in raw_data.keys():
        customerMasterHeader.effective_from = raw_data['effective_from']
    if 'effective_to' in raw_data.keys():
        customerMasterHeader.effective_to = raw_data['effective_to']
    if 'last_updated_by' in raw_data.keys():
        customerMasterHeader.last_updated_by = raw_data['last_updated_by']
    
    new_customer_sites = []
    
    for customer_master_site in raw_data['customer_master_sites']:
        for customer_site in customerMasterHeader.sites:
            if 'customer_site_id' in customer_master_site.keys():
                if customer_master_site["customer_site_id"] == customer_site.customer_site_id:
                    if 'customer_site_code' in customer_master_site.keys():
                        customer_site.customer_site_code = customer_master_site['customer_site_code']
                    if 'customer_address' in customer_master_site.keys():
                        customer_site.customer_address = customer_master_site['customer_address']
                    if 'phone_number1' in customer_master_site.keys():
                        customer_site.phone_number1 = customer_master_site['phone_number1']
                    if 'phone_number2' in customer_master_site.keys():
                        customer_site.phone_number2 = customer_master_site['phone_number2']
                    if 'email' in customer_master_site.keys():
                        customer_site.email = customer_master_site['email']
                    if 'effective_from' in customer_master_site.keys():
                        customer_site.effective_from = customer_master_site['effective_from']
                    if 'effective_to' in customer_master_site.keys():
                        customer_site.effective_to = customer_master_site['effective_to']
                    if 'last_updated_by' in customer_master_site.keys():
                        customer_site.last_updated_by = customer_master_site['last_updated_by'] 
                    break
            else:
                new_customer_site = CustomerMasterSites()
                if 'customer_site_code' in customer_master_site.keys():
                    new_customer_site.customer_site_code = customer_master_site['customer_site_code']
                if 'customer_address' in customer_master_site.keys():
                    new_customer_site.customer_address = customer_master_site['customer_address']
                if 'phone_number1' in customer_master_site.keys():
                    new_customer_site.phone_number1 = customer_master_site['phone_number1']
                if 'phone_number2' in customer_master_site.keys():
                    new_customer_site.phone_number2 = customer_master_site['phone_number2']
                if 'email' in customer_master_site.keys():
                    new_customer_site.email = customer_master_site['email']
                if 'effective_from' in customer_master_site.keys():
                    new_customer_site.effective_from = customer_master_site['effective_from']
                if 'effective_to' in customer_master_site.keys():
                    new_customer_site.effective_to = customer_master_site['effective_to']
                if 'created_by' in customer_master_site.keys():
                    new_customer_site.created_by = customer_master_site['created_by']
                if 'last_updated_by' in customer_master_site.keys():
                    new_customer_site.last_updated_by = customer_master_site['last_updated_by']   
                new_customer_sites.append(new_customer_site)
                break
                
    if len(new_customer_sites) > 0:
        customerMasterHeader.sites.extend(new_customer_sites)
        
@db_transaction
def get_customer_detail(customer_code,session):
    customerheader = session.query(CustomerMasterHeader).filter_by(customer_code=customer_code).first()
    result = dict(customerheader.__dict__)
    result.pop('_sa_instance_state')
    line_dicts = []
    for line in customerheader.sites:
        line_dict = dict(line.__dict__)
        line_dict.pop('_sa_instance_state')
        line_dicts.append(line_dict)
    result['customer_master_sites'] = line_dicts
    return result           
    