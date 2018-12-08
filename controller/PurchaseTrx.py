'''
Created on 23-Nov-2018

@author: duttasudip89
'''

import json
import falcon
import logging
from dao.PurchaseTrx import create_purchase_trx, update_purchase_trx
from dao.PurchaseTrx import get_purchase_transaction_details
from schema.PurchaseTrxSchema import PurchaseTrxHeaderSchema,PurchaseTrxHeaderUpdateSchema


class PurchaseTrx(object):
    
    serializers = { 'post': PurchaseTrxHeaderSchema,
                    'put': PurchaseTrxHeaderUpdateSchema
                    }
    
    def on_post(self, req, resp):
        try:
            """
            Insert Purchase Transaction data into database
            """
            data = req.context['serialized-data']
            create_purchase_trx(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Purchase Transaction data saved successfully for: " + data['purchase_trx_number']}
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
            
        if 'purchase_trx_number' in params.keys():
            purchase_trx_details = get_purchase_transaction_details(params)
        else:
            purchase_trx_details = get_purchase_transaction_details(None)
        
        payload['purchase_trx_details'] = purchase_trx_details
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        return resp 
        
        
    def on_put(self,req, resp):
        try:
            """
            update Purchase Transaction data into database
            """ 
            data = req.context['serialized-data']  
                
            update_purchase_trx(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Purchase Transaction data updated successfully for: " + data['purchase_trx_number']}
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
>>>>>>> 789c999a7d1e539b538e65e3d399ce20af4fb60b
