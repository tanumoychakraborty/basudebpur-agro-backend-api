'''
Created on 28-Nov-2018

@author: tanumoy
'''
from marshmallow.exceptions import ValidationError
from util.HTTPError import HTTPError
from falcon import status_codes
import json
import sys

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
            print('incoming >>>>>>>>>>>>> '+str(req.headers))
            req_data = json.loads(req.media)
            
        try:
            serializer = resource.serializers[req.method.lower()]
        except (AttributeError, IndexError, KeyError):
            return
        else:
            try:
                req.context['serialized-data'] = serializer().load(
                    data=req_data
                )
                print('serialized data type >>>>>>>>>>' , type(req.context['serialized-data']))
                print('serialized data string >>>>>>>>>>' , str(req.context['serialized-data']))
                print('serialized data >>>>>>>>>>' , req.context['serialized-data'])
            except ValidationError as err:
                print('validation error >>>>>>>>>>'+str(err.messages))
                raise HTTPError(status=status_codes.HTTP_422, errors=err.messages)
            except:
                print("Unexpected error >>>>>>>>>>>>>", sys.exc_info()[0])
                raise
