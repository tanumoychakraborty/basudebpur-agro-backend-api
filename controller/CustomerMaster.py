'''
Created on 06-Apr-2019

@author: duttasudip89
'''

from dao.CustomerMaster import get_customer_details
from dao.CustomerMaster import create_customer,update_customer,search_customer_details, get_customer_detail
import json
import falcon
import logging
from schema.CustomerMasterSchema import CustomerMasterHeaderSchema,CustomerMasterHeaderUpdateSchema
from dao.Users import get_user_id_by_user_name


class CustomerMaster(object):
    serializers = { 'post': CustomerMasterHeaderSchema,
                    'put':  CustomerMasterHeaderUpdateSchema
                    }
    
    def on_post(self, req, resp):
        try:
            """
            Insert customer data into database
            """
            data = req.context['serialized-data']
            user = get_user_id_by_user_name(data['created_by'])
            data['last_updated_by'] = user
            data['created_by'] = user
            for line in data['customer_master_sites']:
                line['last_updated_by'] = user
                line['created_by'] = user
            create_customer(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Customer Details saved successfully for: " + data['customer_name']}
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
        params= req.params
        payload = {}
        OperationType = params.get('OperationType',None)
        if OperationType == "CUSTOMER_LIST":
            customerLists = get_customer_details()
            if customerLists is None:
                resp.status = falcon.HTTP_404
                return
            payload['customerLists'] = customerLists
        if OperationType == "CUSTOMER_MASTER_SEARCH":
                customer_details = search_customer_details(params,0,None)
                payload['customer_details'] = customer_details
        if list(params.keys()) == ['customer_code']:
                customer_details = [get_customer_detail(params['customer_code'])]        
                for customer_detail in customer_details:
                    for key, value in customer_detail.items():
                        if value is None:
                            customer_detail[key] = ''
                        
                payload['customer_details'] = customer_details   
            
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        
    def on_put(self,req, resp):
        try:
            """
            update customer data into database
            """ 
            data = req.context['serialized-data']  
            data['last_updated_by'] = get_user_id_by_user_name(data['created_by'])
            for line in data['customer_master_sites']:
                line['last_updated_by'] = get_user_id_by_user_name(data['created_by'])
                if 'customer_site_id' not in line.keys():
                    line['created_by'] = get_user_id_by_user_name(data['created_by'])
                    line['last_updated_by'] = get_user_id_by_user_name(data['created_by'])
            update_customer(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Customer data updated successfully for: " + data['customer_code']}
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
