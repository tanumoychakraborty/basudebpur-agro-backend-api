'''
Created on 30-Oct-2018

@author: tanumoy
'''
from dao.Users import get_user_type_by_user_id
from dao.AccessRights import get_access_rights_by_user_type
import json
import falcon

class AccessRights(object):
    '''
    different calls on Access Rights resource 
    '''


    def on_get(self,req, resp):
        params = req.params
        payload = {}        
        if 'userId' in params.keys():
            userid = int(params['userId'])
            usertype = get_user_type_by_user_id(userid)
            payload['access'] = get_access_rights_by_user_type(usertype)
            
        elif 'userType' in params.keys():
            payload['access'] = (get_access_rights_by_user_type(params['usertype']))
            
        
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200