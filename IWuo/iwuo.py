import web
import blog

urls = (
        '/','Home',
        '/blog', blog.blog_app,
        '/mail','Mail'
        )
class Home:
    def GET(self):
        return 'Home'


class Mail:
    def GET(self):
        web.config.smtp_server = 'smtp.gmail.com'
        web.config.smtp_port = 587
        web.config.smtp_username = 'liyajie1209@gmail.com'
        web.config.smtp_password = 'passwor'
        web.config.smtp_starttls = True
        web.sendmail('liyajie1209@gmail.com','365283170@qq.com','message','message content')


app = web.application(urls,locals())

if __name__ == '__main__':
    app.run()
