'''
Created on 31-Jul-2019

@author: duttasudip89
'''

import json
import falcon
from dao.Receipt import  create_challan, update_challan
from schema.ReceiptSchema import ReceiptHeaderSchema ,ReceiptHeaderUpdateSchema
from dao.Users import get_user_id_by_user_name


class Challan(object):
    
    
    serializers = { 'post': ReceiptHeaderSchema,
                     'put': ReceiptHeaderUpdateSchema
                    }
                   
    
    def on_post(self, req, resp):
        try:
            """
            Insert Challan Data in database
            """
            data = req.context['serialized-data']
            user = get_user_id_by_user_name(data['created_by'])
            data['last_updated_by'] = user
            data['created_by'] = user
            create_challan(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Challan created. "}
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
        
    def on_put(self,req, resp):
        try:
            """
            update Receipt data into database
            """ 
            data = req.context['serialized-data']  
            update_challan(data)
            output = {'Status': falcon.HTTP_200, 'Message': "Challan data updated successfully for " + data['challan_number']}
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