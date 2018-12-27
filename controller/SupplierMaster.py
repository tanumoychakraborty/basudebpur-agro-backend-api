'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from dao.SupplierMaster import get_supplier_details
from dao.SupplierMaster import create_supplier,update_supplier,search_supplier_details,get_supplier_detail
import json
import falcon
import logging
from schema.SupplierMasterSchema import SupplierMasterHeaderSchema,SupplierMasterHeaderUpdateSchema
from dao.Users import get_user_id_by_user_name


class SupplierMaster(object):
    serializers = { 'post': SupplierMasterHeaderSchema,
                    'put':  SupplierMasterHeaderUpdateSchema
                    }
    
    def on_post(self, req, resp):
        try:
            """
            Insert Purchase Transaction data into database
            """
            data = req.context['serialized-data']
            user = get_user_id_by_user_name(data['created_by'])
            data['last_updated_by'] = user
            data['created_by'] = user
            for line in data['supplier_master_sites']:
                line['last_updated_by'] = user
                line['created_by'] = user
            create_supplier(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Supplier Details saved successfully for: " + data['supplier_name']}
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
        if OperationType == "SUPPLIER_LIST":
            supplierLists = get_supplier_details()
            if supplierLists is None:
                resp.status = falcon.HTTP_404
                return
            payload['supplierLists'] = supplierLists
        if OperationType == "SUPPLIER_MASTER_SEARCH":
                supplier_details = search_supplier_details(params,0,None)
                payload['supplier_details'] = supplier_details
        if list(params.keys()) == ['supplier_code']:
                supplier_details = [get_supplier_detail(params['supplier_code'])]        
                for supplier_detail in supplier_details:
                    for key, value in supplier_detail.items():
                        if value is None:
                            supplier_detail[key] = ''
                        
                payload['supplier_details'] = supplier_details   
            
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        
    def on_put(self,req, resp):
        try:
            """
            update supplier data into database
            """ 
            data = req.context['serialized-data']  
            user = get_user_id_by_user_name(data['last_updated_by'])
            data['last_updated_by'] = user
            for line in data['supplier_master_sites']:
                line['last_updated_by'] = user
            update_supplier(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Supplier data updated successfully for: " + data['supplier_code']}
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