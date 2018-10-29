import falcon
#from test import test
import json
from sqlalchemy.orm.session import sessionmaker
from model import test
from dbEngine import dbEngine
from sqlalchemy.orm.scoping import scoped_session
from dao.AccessRights import get_access_rights_by_access_id

class testview(object):

	def on_get(self, req, resp):
		payload = {}
		payload['msg'] = 'test text'
		
		resp.body = json.dumps(payload)
		resp.status = falcon.HTTP_200
		access = get_access_rights_by_access_id(10)
		print(access)
		
# 		session_factory = sessionmaker(bind=dbEngine.get())
# 		Session = scoped_session(session_factory)
# 		local_session = Session()
# 		newtest = test.test(test='test column')
# 		local_session.add(newtest)
# 		local_session.commit()
# 		local_session.remove()

api = application = falcon.API()
t = testview()
api.add_route('/test', t)


# class abstr:
# 	pass
# a=abstr()
# a.x=1
# a.y=2