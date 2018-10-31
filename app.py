from test import testview
import falcon
from controller.AccessRights import AccessRights


api = application = falcon.API()
t = testview()
a = AccessRights()
api.add_route('/api/test', t)
api.add_route('/api/access-right', a)

