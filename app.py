from test import testview
import falcon
from controller.AccessRights import AccessRights
from controller.PurchaseTrx import PurchaseTrx
from controller.CommonLookups import CommonLookups
from controller.SupplierMaster import SupplierMaster
from controller.InventoryItems import InventoryItems
from util.SerializerMiddleware import SerializerMiddleware


api = application = falcon.API(middleware=[SerializerMiddleware(),])
t = testview()
a = AccessRights()
purchase_trx =PurchaseTrx()
common_lookups =CommonLookups()
supplier_master = SupplierMaster()
inventory_items = InventoryItems()
api.add_route('/api/test', t)
api.add_route('/api/access-right', a)
api.add_route('/api/purchase_trx', purchase_trx)
api.add_route('/api/common_lookups', common_lookups)
api.add_route('/api/supplier_master', supplier_master)
api.add_route('/api/inventory_items', inventory_items)


