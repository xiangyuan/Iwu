import web
import blog

urls = (
        '/','Home',
        '/blog', blog.blog_app,
        )
class Home:
    def GET(self):
        return 'Home'


app = web.application(urls,locals())

if __name__ == '__main__':
    app.run()
