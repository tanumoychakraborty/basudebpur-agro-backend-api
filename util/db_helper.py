'''
Created on 28-Oct-2018

@author: tanumoy
'''
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from util.dbEngine import dbEngine
import logging
import traceback
import sys


def db_transaction(func):
    def __transaction__(*args,**kwargs):
        Session = scoped_session(sessionmaker(bind=dbEngine.get()))
#         local_session = Session()
#         new_local_session = local_session()
        kwargs['session'] = Session
        
        try:
            result = func(*args,**kwargs)
            Session.commit()
            
            
        except Exception as e:
            Session.rollback()
            traceback.print_exc(file=sys.stdout)
            logging.error(traceback.print_exc())
            raise e
            
        finally:
            Session.remove()
            return result
            
    return __transaction__            
