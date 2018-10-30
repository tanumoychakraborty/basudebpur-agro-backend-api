from test import testview
import falcon
from controller.AccessRights import AccessRights


api = application = falcon.API()
t = testview()
a = AccessRights()
api.add_route('/test', t)
api.add_route('/access-right', a)

