import logging

        
if __name__ == "__main__":
    logging.basicConfig(filename='basudebpur-agro-backend-api.log',filemode='a',format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)
    from gunicorn.app.wsgiapp import WSGIApplication
    logging.info('starting gunicorn server')
    app = WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]")
    logging.info('loading app - %(prog)s [OPTIONS] [APP_MODULE]')
    #app.app_uri = 'basudebpur-agro-backend-api:app'
    app.run()
    logging.info('running %[APP_MODULE]s app in gunicorn server...')