'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from dao.InventoryItems import get_item_details
import json
import falcon
import logging

class InventoryItems(object):
    '''
    different calls on item details 
    '''


    def on_get(self,req, resp):
        params = req.params
        payload = {}  
        OperationType =params['OperationType']      
        if OperationType == "ITEM_LIST":
            itemDetails = get_item_details()
            if itemDetails is None:
                resp.status = falcon.HTTP_404
                return
            payload['itemDetailsList'] = itemDetails
                    
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200