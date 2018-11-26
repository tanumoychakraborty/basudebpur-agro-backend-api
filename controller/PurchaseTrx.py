'''
Created on 23-Nov-2018

@author: duttasudip89
'''

import json
import falcon
import logging
from dao.PurchaseTrx import create_purchase_trx


class PurchaseTrx(object):
        
    def on_post(self, req, resp):
        try:
            """
            Insert Purchase Transaction data into database
            """
            
            raw_json = req.stream.read()
            raw_data = json.loads(raw_json.decode("utf-8"))
            
            create_purchase_trx(raw_data)
            output = {'Status': falcon.HTTP_200, 'Message': "Purchase Transaction data saved successfully for: " + raw_data['purchase_trx_number']}
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
