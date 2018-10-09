
        
if __name__ == "__main__":
    from gunicorn.app.wsgiapp import WSGIApplication
    
    app = WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]")

    #app.app_uri = 'basudebpur-agro-backend-api:app'
    app.run()