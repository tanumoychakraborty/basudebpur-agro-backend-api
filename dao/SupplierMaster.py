'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from model.SupplierMasterHeader import SupplierMasterHeader
from model.SupplierMasterSites import SupplierMasterSites
from util.db_helper import db_transaction


@db_transaction
def get_supplier_details(session):
    resultL = []
    supplierDetails = session.query(SupplierMasterHeader.supplier_id,SupplierMasterHeader.supplier_name,SupplierMasterHeader.description,SupplierMasterHeader.supplier_code
                                           ,SupplierMasterHeader.supplier_type,SupplierMasterSites.supplier_site_id,SupplierMasterSites.supplier_site_code
                                           ).join(SupplierMasterSites,SupplierMasterHeader.enabled_flag=='Y').all()
                  
    for supplierDetail in supplierDetails:
        dict ={ }
        dict['supplier_id'] = supplierDetail[0]
        dict['supplier_name'] = supplierDetail[1]
        dict['description'] = supplierDetail[2]
        dict['supplier_code'] = supplierDetail[3]
        dict['supplier_type'] = supplierDetail[4]
        dict['supplier_site_id'] = supplierDetail[5]
        dict['supplier_site_code'] = supplierDetail[6]
        
        resultL.append(dict)    
            
    return resultL
