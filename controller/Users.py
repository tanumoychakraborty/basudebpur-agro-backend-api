'''
Created on 03-Jan-2019

@author: duttasudip89
'''
import json
import falcon
import logging
from dao.Users import create_user,search_user_details,get_user_detail,update_user
from schema.UsersSchema import UsersSchema,UsersSchemaUpdate
from dao.Users import get_user_id_by_user_name

class Users(object):
    
    
    serializers = { 'post': UsersSchema,
                    'put' : UsersSchemaUpdate
                    }
                   
    
    def on_post(self, req, resp):
        try:
            """
            insert user details into database
            """
            data = req.context['serialized-data']
            create_user(data)
            output = {'Status': falcon.HTTP_200, 'Message': "User Details saved successfully for: " + data['user_name']}
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
        
        if OperationType == "USER_SEARCH":
                user_details = search_user_details(params,0,None)
                payload['user_details'] = user_details
        if list(params.keys()) == ['user_name']:
                user_details = [get_user_detail(params['user_name'])]        
                for user_detail in user_details:
                    for key, value in user_detail.items():
                        if value is None:
                            user_detail[key] = ''
                        
                payload['user_details'] = user_details   
            
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200
        
    def on_put(self,req, resp):
        try:
            """
            update user data into database
            """ 
            data = req.context['serialized-data']
            update_user(data)
            output = {'Status': falcon.HTTP_200, 'Message': "User data updated successfully for: " + data['user_name']}
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