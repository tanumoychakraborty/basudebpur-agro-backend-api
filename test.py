import falcon
import json


class testview(object):

	def on_get(self, req, resp):
		payload = {}
		payload['msg'] = 'test text'
		
		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
		return resp