'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from dao.SupplierMaster import get_supplier_details
import json
import falcon
import logging

class SupplierMaster(object):
    '''
    different calls on Access Rights resource 
    '''


    def on_get(self,req, resp):
        params= req.params
        payload = {}
        OperationType =params['OperationType']
        if OperationType == "SUPPLIER_LIST":
            supplierLists = get_supplier_details()
            if supplierLists is None:
                resp.status = falcon.HTTP_404
                return
            payload['supplierLists'] = supplierLists
            
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200