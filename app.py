from blog.blog import blog_app
from IWuo.iwuo import iwuo_app
import web


urls = (
        '/','Index',
        '/blog',blog_app,
        '/iwuo',iwuo_app
        )

class Index:
    def GET(self):
        return "Hello Home"



index_app = web.application(urls, globals())

if __name__ == '__main__':
    index_app.run()
