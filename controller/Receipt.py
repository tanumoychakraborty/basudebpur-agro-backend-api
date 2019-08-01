'''
Created on 19-jul-2019

@author: duttasudip89
'''

import json
import falcon
import logging
from dao.Receipt import update_receipt_data,\
    get_receipt_details,get_receipt_detail,\
    get_receipt_detail_by_receipt_header_id
from schema.ReceiptSchema import ReceiptHeaderUpdateSchema


class Receipt(object):
    
    
    serializers = { 
                    'put': ReceiptHeaderUpdateSchema
                    }
                   
    def on_get(self,req, resp):
        
        params = req.params
        payload = {}        
            
        if params.keys():
            if list(params.keys()) == ['receipt_number']:
                receipt_details = [get_receipt_detail(params['receipt_number'])]
            elif list(params.keys()) == ['receipt_header_id']:
                receipt_details = [get_receipt_detail_by_receipt_header_id(params['receipt_header_id'])]
            else:
                receipt_details = get_receipt_details(params,0,None)
        else:
            receipt_details = get_receipt_details(None,0,None)
        
        for receipt_detail in receipt_details:
            for key, value in receipt_detail.items():
                if value is None:
                    value = ''
                    receipt_detail[key] = value
            
        payload['receipt_details'] = receipt_details
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        return resp
    
    def on_put(self,req, resp):
        try:
            """
            update Receipt data into database
            """ 
            data = req.context['serialized-data']  
            update_receipt_data(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Receipt data updated successfully for "}
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
        
        
    
