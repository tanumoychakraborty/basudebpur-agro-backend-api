'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from model.SupplierMasterHeader import SupplierMasterHeader
from model.SupplierMasterSites import SupplierMasterSites
from util.db_helper import db_transaction
from sqlalchemy.sql.expression import and_


@db_transaction
def get_supplier_details(session):
    resultL = []
#     supplierDetails = session.query(SupplierMasterHeader.supplier_id,SupplierMasterHeader.supplier_name,SupplierMasterHeader.description,SupplierMasterHeader.supplier_code
#                                            ,SupplierMasterHeader.supplier_type,SupplierMasterSites.supplier_site_id,SupplierMasterSites.supplier_site_code
#                                            ).join(SupplierMasterSites,SupplierMasterHeader.enabled_flag=='Y').all()
    supplierDetails = session.query(SupplierMasterHeader).all()
                  
    for supplierDetail in supplierDetails:
        dict = { }
        dict['supplier_id'] = supplierDetail.supplier_id
        dict['supplier_name'] = supplierDetail.supplier_name
        dict['description'] = supplierDetail.description
        dict['supplier_code'] = supplierDetail.supplier_code
        dict['supplier_type'] = supplierDetail.supplier_type
#         dict['supplier_site_id'] = supplierDetail[5]
#         dict['supplier_site_code'] = supplierDetail[6]
        resultL.append(dict) 

            
    return resultL

@db_transaction
def create_supplier(raw_data, session):
    supplierMasterHeader = SupplierMasterHeader()
    supplierMasterHeader.supplier_code = raw_data['supplier_code']
    supplierMasterHeader.supplier_name = raw_data['supplier_name']
    supplierMasterHeader.description = raw_data['description']
    supplierMasterHeader.supplier_type = raw_data['supplier_type']
    supplierMasterHeader.remarks = raw_data['remarks']
    supplierMasterHeader.enabled_flag = raw_data['enabled_flag']
    supplierMasterHeader.effective_from = raw_data['effective_from']
    supplierMasterHeader.effective_to = raw_data['effective_to']
#    supplierMasterHeader.employee_id = raw_data['employee_id'] future use
#    supplierMasterHeader.ship_to_location_code = raw_data['ship_to_location_code']
#    SupplierMasterHeader.bill_to_location_code = raw_data['bill_to_location_code']
    supplierMasterHeader.created_by = raw_data['created_by']
    supplierMasterHeader.last_updated_by = raw_data['last_updated_by'] 
        
    SupplierMasterSitesList = []
    for supplier_master_Site in raw_data['supplier_master_sites']:
        SupplierMasterSite = SupplierMasterSites()
        SupplierMasterSite.supplier_site_code = supplier_master_Site['supplier_site_code']
        SupplierMasterSite.supplier_site_address = supplier_master_Site['supplier_site_address']
        SupplierMasterSite.phone_number1 = supplier_master_Site['phone_number1']
        SupplierMasterSite.phone_number2 = supplier_master_Site['phone_number2']
        SupplierMasterSite.email = supplier_master_Site['email']
        '''
        SupplierMasterSite.payment_method_lookup_code = Supplier_Master_Site['payment_method_lookup_code']
        SupplierMasterSite.gstin_number = Supplier_Master_Site['gstin_number']
        SupplierMasterSite.pay_group_lookup_code = Supplier_Master_Site['pay_group_lookup_code']
        other fields also need to include
        '''
        SupplierMasterSite.inactive_date = supplier_master_Site['inactive_date']
        SupplierMasterSite.created_by = supplier_master_Site['created_by']
        SupplierMasterSite.last_updated_by = supplier_master_Site['last_updated_by']   
        SupplierMasterSitesList.append(SupplierMasterSite)
            
    supplierMasterHeader.sites = SupplierMasterSitesList
     
    session.add(supplierMasterHeader)
    
    return SupplierMasterHeader

@db_transaction
def update_supplier(raw_data,session):
    supplier_code = raw_data['supplier_code']
 #   supplier_id = raw_data['supplier_id']
    supplierMasterHeader = session.query(SupplierMasterHeader).filter_by(supplier_code=supplier_code).first()
    
    supplierMasterHeader.supplier_name = raw_data['supplier_name']
    supplierMasterHeader.description = raw_data['description']
    supplierMasterHeader.supplier_type = raw_data['supplier_type']
    supplierMasterHeader.remarks = raw_data['remarks']
    supplierMasterHeader.enabled_flag = raw_data['enabled_flag']
    supplierMasterHeader.effective_from = raw_data['effective_from']
    supplierMasterHeader.effective_to = raw_data['effective_to']
#    supplierMasterHeader.employee_id = raw_data['employee_id'] future use
#    supplierMasterHeader.ship_to_location_code = raw_data['ship_to_location_code']
#    SupplierMasterHeader.bill_to_location_code = raw_data['bill_to_location_code']
    #supplierMasterHeader.created_by = raw_data['created_by']
    supplierMasterHeader.last_updated_by = raw_data['last_updated_by']
    
    new_supplier_sites = []
    
    for supplier_master_site in raw_data['supplier_master_sites']:
        for supplier_site in supplierMasterHeader.sites:
            if 'supplier_site_id' in supplier_master_site.keys():
                if supplier_master_site["supplier_site_id"] == supplier_site.supplier_site_id:
                    supplier_site.supplier_site_code = supplier_master_site['supplier_site_code']
                    supplier_site.supplier_site_address = supplier_master_site['supplier_site_address']
                    supplier_site.phone_number1 = supplier_master_site['phone_number1']
                    supplier_site.phone_number2 = supplier_master_site['phone_number2']
                    supplier_site.email = supplier_master_site['email']
                    '''
                    supplier_site.payment_method_lookup_code = Supplier_Master_Site['payment_method_lookup_code']
                    supplier_site.gstin_number = Supplier_Master_Site['gstin_number']
                    supplier_site.pay_group_lookup_code = Supplier_Master_Site['pay_group_lookup_code']
                    other fields also need to include
                    '''
                    supplier_site.inactive_date = supplier_master_site['inactive_date']
                    #supplier_site.created_by = supplier_master_site['created_by']
                    supplier_site.last_updated_by = supplier_master_site['last_updated_by'] 
                    break
            else:
                SupplierMasterSite = SupplierMasterSites()
                SupplierMasterSite.supplier_site_code = supplier_master_site['supplier_site_code']
                SupplierMasterSite.supplier_site_address = supplier_master_site['supplier_site_address']
                SupplierMasterSite.phone_number1 = supplier_master_site['phone_number1']
                SupplierMasterSite.phone_number2 = supplier_master_site['phone_number2']
                SupplierMasterSite.email = supplier_master_site['email']
                '''
                SupplierMasterSite.payment_method_lookup_code = Supplier_Master_Site['payment_method_lookup_code']
                SupplierMasterSite.gstin_number = Supplier_Master_Site['gstin_number']
                SupplierMasterSite.pay_group_lookup_code = Supplier_Master_Site['pay_group_lookup_code']
                other fields also need to include
                '''
                SupplierMasterSite.inactive_date = supplier_master_site['inactive_date']
                SupplierMasterSite.created_by = supplier_master_site['created_by']
                SupplierMasterSite.last_updated_by = supplier_master_site['last_updated_by']   
                new_supplier_sites.append(SupplierMasterSite)
                break
                
    if len(new_supplier_sites) > 0:
        supplierMasterHeader.sites.extend(new_supplier_sites)
                
@db_transaction
def search_supplier_details(params,page, page_size,session):
        resultL = []
        supplier_code = params.get('supplier_code',None)
        supplier_name = params.get('supplier_name',None)
        supplier_type = params.get('supplier_type',None)
        
        supplierDetails = session.query(SupplierMasterHeader.supplier_code,SupplierMasterHeader.supplier_name,
                                           SupplierMasterHeader.description,SupplierMasterHeader.supplier_type,SupplierMasterHeader.enabled_flag)
         
        conditions = []
        if supplier_code:
            conditions.append(SupplierMasterHeader.supplier_code == supplier_code)
        if supplier_name:
            conditions.append(SupplierMasterHeader.supplier_name == supplier_name)
        if supplier_type:
            conditions.append(SupplierMasterHeader.supplier_type == supplier_type)
            
                
        supplierDetails = supplierDetails.filter(and_(*conditions)).all()   
        
        if page_size:
            supplierDetails = supplierDetails.limit(page_size)
        if page: 
            supplierDetails = supplierDetails.offset(page*page_size) 
                  
        for supplierDetail in supplierDetails:
            dict ={ }
            dict['supplier_code'] = supplierDetail[0]
            dict['supplier_name'] = supplierDetail[1]
            dict['description'] = supplierDetail[2]
            dict['supplier_type'] = supplierDetail[3]
            dict['enabled_flag'] = supplierDetail[4]
            
            resultL.append(dict)    
                
        return resultL 
    
@db_transaction
def get_supplier_detail(supplier_code,session):
    supplierheader = session.query(SupplierMasterHeader).filter_by(supplier_code=supplier_code).first()
    result = dict(supplierheader.__dict__)
    result.pop('_sa_instance_state')
    line_dicts = []
    for line in supplierheader.sites:
        line_dict = dict(line.__dict__)
        line_dict.pop('_sa_instance_state')
        line_dicts.append(line_dict)
    result['supplier_master_sites'] = line_dicts
    return result                    
