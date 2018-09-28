import falcon
#from test import test
import json

class test(object):

	def on_get(self, req, resp):
		payload = {}
		payload['msg'] = 'test text'

		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200

api = application = falcon.API()
t = test()
api.add_route('/test', t)


# class abstr:
# 	pass
# a=abstr()
# a.x=1
# a.y=2