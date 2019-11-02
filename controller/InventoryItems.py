'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from dao.InventoryItems import get_item_details
import json
import falcon
import logging
from dao.Users import get_user_id_by_user_name
from dao.InventoryItems import create_items,update_items,search_item_details,get_item_detail
from schema.InventoryItemsSchema import InventoryItemsSchema,InventoryItemsUpdateSchema

class InventoryItems(object):
    serializers = { 'post': InventoryItemsSchema,
                    'put':  InventoryItemsUpdateSchema
                    }
    '''
    different calls on item details 
    '''

    def on_post(self, req, resp):
        try:
            
            data = req.context['serialized-data']
            user = get_user_id_by_user_name(data['created_by'])
            data['last_updated_by'] = user
            data['created_by'] = user
            create_items(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Item Details saved successfully for: " + data['item_number']}
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output)
  
        except (KeyError, ValueError) as e:
            error = "{err} field is required..!".format(err=e) 
            resp.body = json.dumps({"Status": falcon.HTTP_400, 'Error':str(error)})
            resp.status = falcon.HTTP_400

        except Exception as e:
            resp.body = json.dumps({"Status": falcon.HTTP_400, 'Error':str(e)})
            resp.status = falcon.HTTP_400
            return resp  
    def on_get(self,req, resp):
        params = req.params
        payload = {}  
        OperationType = params.get('OperationType',None)  
        source = params.get('source',None)  
        if OperationType == "ITEM_LIST":
            if source == 'PURCHASE':
                itemDetails = search_item_details({'item_type':'PADDY'},0,None)
            elif source == 'SALES':
                itemDetails = search_item_details({'item_type': ['RICE']},0,None)
            if itemDetails is None:
                resp.status = falcon.HTTP_404
                return
            payload['itemDetailsList'] = itemDetails
        if OperationType == "ITEM_MASTER_SEARCH":
                item_details = search_item_details(params,0,None)
                payload['item_details'] = item_details
        if list(params.keys()) == ['item_id']:
                item_details = [get_item_detail(params['item_id'])]        
                for item_detail in item_details:
                    for key, value in item_detail.items():
                        if value is None:
                            item_detail[key] = ''
                        
                payload['item_details'] = item_details   
            
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200    
                    
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        
    def on_put(self,req, resp):
        try:
            """
            update item data into database
            """ 
            data = req.context['serialized-data']  
            user = get_user_id_by_user_name(data['last_updated_by'])
            data['last_updated_by'] = user
            update_items(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Item Details updated successfully for: " + data['item_number']}
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output)
            
        
        except (KeyError, ValueError) as e:
            error = "{err} field is required..!".format(err=e) 
            resp.body = json.dumps({"Status": falcon.HTTP_400, 'Error':str(error)})
            resp.status = falcon.HTTP_400

        except Exception as e:
            resp.body = json.dumps({"Status": falcon.HTTP_400, 'Error':str(e)})
            resp.status = falcon.HTTP_400
            return resp       