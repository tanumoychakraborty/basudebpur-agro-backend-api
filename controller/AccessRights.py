'''
Created on 30-Oct-2018

@author: tanumoy
'''
from dao.Users import get_user_type_by_user_id,\
    get_user_type_by_username_password
from dao.AccessRights import get_access_rights_by_user_type
import json
import falcon
import logging

class AccessRights(object):
    '''
    different calls on Access Rights resource 
    '''


    def on_get(self,req, resp):
        params = req.params
        payload = {}        
        if 'userName' and 'password' in params.keys():
            usertype = get_user_type_by_username_password(params['userName'], params['password'])
            if usertype is None:
                resp.status = falcon.HTTP_404
                return
            payload['access'] = usertype
                        
        elif 'userId' in params.keys():
            userid = int(params['userId'])
            usertype = get_user_type_by_user_id(userid)
            if usertype is None:
                resp.status = falcon.HTTP_404
                return
            payload['access'] = get_access_rights_by_user_type(usertype)
            
        elif 'userType' in params.keys():
            accessright = get_access_rights_by_user_type(params['userType'])
            if accessright is None:
                resp.status = falcon.HTTP_404
                return
            payload['access'] = accessright
        
        resp.body = json.dumps(payload, indent=4, sort_keys=True, default=str)
        resp.status = falcon.HTTP_200