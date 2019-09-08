'''
Created on 23-Nov-2018

@author: duttasudip89
'''

import json
import falcon
import logging
from dao.SalesTrx import create_sales_trx, update_sales_trx,\
    get_sales_trx_detail
from dao.SalesTrx import get_sales_transaction_details
from schema.SalesTrxSchema import SalesTrxHeaderSchema,SalesTrxHeaderUpdateSchema
from dao.Users import get_user_id_by_user_name, get_user_name_by_user_id
from dao.Receipt import get_receipt_details


class SalesTrx(object):
    
    
    serializers = { 'post': SalesTrxHeaderSchema,
                    'put': SalesTrxHeaderUpdateSchema
                    }
                   
    
    def on_post(self, req, resp):
        try:
            """
            Insert Sales Transaction data into database
            """
            data = req.context['serialized-data']
            #data['sales_rep_id'] = get_user_id_by_user_name(data['sales_rep_id'])
            user = get_user_id_by_user_name(data['created_by'])
            data['last_updated_by'] = user
            data['sales_rep_id'] = user
            data['created_by'] = user
            for line in data['sales_trx_lines']:
                line['last_updated_by'] = user
                line['created_by'] = user
            create_sales_trx(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Sales Transaction data saved successfully."}
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
                sales_trx_details = [get_sales_trx_detail(params['transaction_number'])]
                sales_trx_details[0]['sales_rep_name'] = get_user_name_by_user_id(sales_trx_details[0]['sales_rep_id'])
                receipt_details = get_receipt_details({'source_transaction_header_id': params['transaction_number']},0,None)
                sales_trx_details[0]['receipt_details'] = receipt_details
                
            else:
                sales_trx_details = get_sales_transaction_details(params,0,None)
        else:
            sales_trx_details = get_sales_transaction_details(None,0,None)
        
        for sales_trx_detail in sales_trx_details:
            for key, value in sales_trx_detail.items():
                if value is None:
                    value = ''
                    sales_trx_detail[key] = value
            
        payload['sales_trx_details'] = sales_trx_details
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        return resp 
        
        
    def on_put(self,req, resp):
        try:
            """
            update sales Transaction data into database
            """ 
            data = req.context['serialized-data']
            update_sales_trx(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Sales Transaction data updated successfully for: " + data['sales_trx_number']}
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
