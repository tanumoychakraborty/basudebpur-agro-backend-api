import falcon
#from test import test
import json
from sqlalchemy.orm.session import sessionmaker
from model import test
from dbEngine import dbEngine

class testview(object):

	def on_get(self, req, resp):
		payload = {}
		payload['msg'] = 'test text'
		
		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
		
		Session = sessionmaker(bind=dbEngine.get())
		session = Session()
		newtest = test.test(test='test column')
		session.add(newtest)
		session.commit()

api = application = falcon.API()
t = testview()
api.add_route('/test', t)


# class abstr:
# 	pass
# a=abstr()
# a.x=1
# a.y=2