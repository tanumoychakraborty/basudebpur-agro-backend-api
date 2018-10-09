import falcon
#from test import test
import json
from test import test


api = application = falcon.API()
t = test()
api.add_route('/test', t)


# class abstr:
# 	pass
# a=abstr()
# a.x=1
# a.y=2