from test import testview
import falcon
from controller.AccessRights import AccessRights
from controller.PurchaseTrx import PurchaseTrx
from controller.CommonLookups import CommonLookups
from controller.SupplierMaster import SupplierMaster
from controller.CustomerMaster import CustomerMaster
from controller.InventoryItems import InventoryItems
from controller.Receipt import Receipt
from controller.Users import Users
from controller.SalesTrx import SalesTrx
from util.SerializerMiddleware import SerializerMiddleware


api = application = falcon.API(middleware=[SerializerMiddleware(),])
t = testview()
a = AccessRights()
purchase_trx =PurchaseTrx()
common_lookups =CommonLookups()
supplier_master = SupplierMaster()
customer_master = CustomerMaster()
inventory_items = InventoryItems()
receipt = Receipt()
users = Users()
sales_trx = SalesTrx()
api.add_route('/api/test', t)
api.add_route('/api/access-right', a)
api.add_route('/api/purchase_trx', purchase_trx)
api.add_route('/api/sales_trx', sales_trx)
api.add_route('/api/common_lookups', common_lookups)
api.add_route('/api/supplier_master', supplier_master)
api.add_route('/api/inventory_items', inventory_items)
api.add_route('/api/customer_master', customer_master)
api.add_route('/api/receipt', receipt)

api.add_route('/api/users',users)


