'''
Created on 21-Dec-2018

@author: duttasudip89
'''
from dao.CommonLookups import get_lookup_values
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
        if lookupName == "PURCHASE_ORDER_HEADER_STATUS":
            headerStatus = get_lookup_values(lookupName)
            if headerStatus is None:
                resp.status = falcon.HTTP_404
                return
            payload['purchaseOrderHeaderStatus'] = headerStatus
            
        if lookupName == "PURCHASE_ORDER_LINES_STATUS":
            lineStatus = get_lookup_values(lookupName)
            if lineStatus is None:
                resp.status = falcon.HTTP_404
                return
            payload['purchaseOrderLineStatus'] = lineStatus
            
        if lookupName == "PURCHASE_ORDER_TYPE":
            poType = get_lookup_values(lookupName)
            if poType is None:
                resp.status = falcon.HTTP_404
                return
            payload['purchaseOrderType'] = poType
            
        if lookupName == "UNIT_OF_MEASURE":
            uom = get_lookup_values(lookupName)
            if uom is None:
                resp.status = falcon.HTTP_404
                return
            payload['UnitOfMeasure'] = uom          
              
            
                    
        
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200