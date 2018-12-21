from test import testview
import falcon
from controller.AccessRights import AccessRights
from controller.PurchaseTrx import PurchaseTrx
from controller.CommonLookups import CommonLookups
from util.SerializerMiddleware import SerializerMiddleware


api = application = falcon.API(middleware=[SerializerMiddleware(),])
t = testview()
a = AccessRights()
purchase_trx =PurchaseTrx()
common_lookups =CommonLookups()
api.add_route('/api/test', t)
api.add_route('/api/access-right', a)
api.add_route('/api/purchase_trx', purchase_trx)
api.add_route('/api/common_lookups', common_lookups)

