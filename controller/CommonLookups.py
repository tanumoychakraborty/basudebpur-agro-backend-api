'''
Created on 21-Dec-2018

@author: duttasudip89
'''
from dao.CommonLookups import get_purchase_order_header_status
import json
import falcon
import logging

class CommonLookups(object):
    '''
    different calls on Access Rights resource 
    '''


    def on_get(self,req, resp):
        params = req.params
        payload = {}  
        lookupName =params['lookupName']      
        if lookupName == "PurchaseOrderHeaderStatus":
            headerStatus = get_purchase_order_header_status()
            if headerStatus is None:
                resp.status = falcon.HTTP_404
                return
            payload['purchaseOrderHeaderStatus'] = headerStatus
                    
        
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200