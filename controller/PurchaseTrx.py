'''
Created on 23-Nov-2018

@author: duttasudip89
'''

from sqlalchemy.orm.session import sessionmaker
from model import PurchaseTrxHeader
from util.dbEngine import dbEngine

import json
import falcon
import logging


class PurchaseTrx(object):
    
    
        
    def on_post(self, req, resp):
        try:
            """
            Insert Purchase Transaction data into database
            """
            
            
            Session = sessionmaker(bind=dbEngine.get())
            session = Session()  
            raw_json = req.stream.read()
            raw_data = json.loads(raw_json.decode("utf-8"))

            transaction_header_data = dict(purchase_trx_number = raw_data['purchase_trx_number'],
               transaction_date = raw_data['transaction_date'],
               order_type = raw_data['order_type'],
               order_status = raw_data['order_status'],
               buyer_id = raw_data['buyer_id'],
               suppplier_id = raw_data['suppplier_id'],
               amount = raw_data['amount'],
               weighting_number = raw_data['weighting_number'],
               created_by = raw_data['created_by'],
               last_updated_by = raw_data['last_updated_by']
                            )
           
           
            seq = session.sequence('apps.purchase_trx_header_sequence')
            nextid = session.execute(seq)
        
            print(nextid)
            transaction_header_data = PurchaseTrxHeader(**transaction_header_data)
            session.add(transaction_header_data)
            # print(movie)
            output = {'Status': falcon.HTTP_200, 'Message': "Purchase Transaction data saved successfully for: "+transaction_header_data.purchase_trx_number}
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output)
            session.commit()                
  
        except (KeyError, ValueError) as e:
            session.rollback()
            error = "{err} field is required..!".format(err=e) 
            resp.body = json.dumps({"Status": falcon.HTTP_400, 'Error':str(error)})
            resp.status = falcon.HTTP_400

        except Exception as e:
            session.rollback()
            resp.body = json.dumps({"Status": falcon.HTTP_400, 'Error':str(e)})
            resp.status = falcon.HTTP_400
            return resp

        finally:
            session.close()
    
        