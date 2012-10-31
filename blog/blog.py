import web

urls = (
        '/','reblog',
        '/about','About'
        )

class reblog:
    def GET(self):
        raise web.seeother('/')
class About:
    def GET(self):
        return 'about' 

    
