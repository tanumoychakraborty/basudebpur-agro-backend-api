'''
Created on 28-Oct-2018

@author: tanumoy
'''
from dbEngine import dbEngine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.scoping import scoped_session


def db_transaction(func):
    def __transaction__(*args,**kwargs):
        Session = scoped_session(sessionmaker(bind=dbEngine.get()))
#         local_session = Session()
#         new_local_session = local_session()
        kwargs['session'] = Session
        
        try:
            func(*args,**kwargs)
            raise Exception('spam', 'eggs')
            Session.commit()
            
            
        except Exception as e:
            Session.rollback()
            print(e)
            #raise
            
        finally:
            Session.remove()
            
    return __transaction__

def local_session():
    session_factory = sessionmaker(bind=dbEngine.get())
    Session = scoped_session(session_factory)
    return Session()