'''
Created on 28-Nov-2018

@author: tanumoy
'''
from marshmallow.exceptions import ValidationError
from util.HTTPError import HTTPError
from falcon import status_codes
import json

class SerializerMiddleware(object):
    '''
    classdocs
    '''

    def process_resource(self, req, resp, resource, params):
        if req.method == 'GET':
            req_data = req.params
        else:
            '''
            for post man
            '''
            #req_data = json.loads(req.stream.read().decode("utf-8"))
            '''
            for django
            '''
            try:
                req_data = json.loads(req.media)
            except TypeError:
                req_data = req.media#json.loads(req.stream.read().decode("utf-8"))
            
        try:
            serializer = resource.serializers[req.method.lower()]
        except (AttributeError, IndexError, KeyError):
            return
        else:
            try:
                req.context['serialized-data'] = serializer().load(
                    data=req_data
                )
            except ValidationError as err:
                raise HTTPError(status=status_codes.HTTP_422, errors=err.messages)