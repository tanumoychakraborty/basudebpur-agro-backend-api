import falcon
import json

class test(object):

	def on_get(self, req, resp):
		payload = {}
		payload['msg'] = 'test text'

		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
