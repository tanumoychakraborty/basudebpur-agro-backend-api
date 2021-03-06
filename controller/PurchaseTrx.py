'''
Created on 23-Nov-2018

@author: duttasudip89
'''

import json
import falcon
import logging
from dao.PurchaseTrx import create_purchase_trx, update_purchase_trx,\
    get_purchase_trx_detail
from dao.PurchaseTrx import get_purchase_transaction_details
from schema.PurchaseTrxSchema import PurchaseTrxHeaderSchema,PurchaseTrxHeaderUpdateSchema
from dao.Users import get_user_id_by_user_name, get_user_name_by_user_id
from dao.Receipt import get_receipt_details


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
            #data['buyer_id'] = get_user_id_by_user_name(data['buyer_id'])
            user = get_user_id_by_user_name(data['created_by'])
            data['last_updated_by'] = user
            data['created_by'] = user
            data['buyer_id'] = user
            for line in data['purchase_trx_lines']:
                line['last_updated_by'] = user
                line['created_by'] = user
            create_purchase_trx(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Purchase Transaction data saved successfully."}
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
            
        if params.keys():
            if list(params.keys()) == ['transaction_number']:
                purchase_trx_details = [get_purchase_trx_detail(params['transaction_number'])]
                purchase_trx_details[0]['buyer_name'] = get_user_name_by_user_id(purchase_trx_details[0]['buyer_id'])
                receipt_details = get_receipt_details({'source_transaction_header_id': params['transaction_number']},0,None)
                purchase_trx_details[0]['receipt_details'] = receipt_details
                
            else:
                purchase_trx_details = get_purchase_transaction_details(params,0,None)
        else:
            purchase_trx_details = get_purchase_transaction_details(None,0,None)
        
        for purchase_trx_detail in purchase_trx_details:
            for key, value in purchase_trx_detail.items():
                if value is None:
                    value = ''
                    purchase_trx_detail[key] = value
            
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


