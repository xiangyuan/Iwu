import web
import blog

urls = (
        '/','Home',
        '/mail','Mail',
        '/db','OpenDb'
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


class OpenDb:
    def GET(self):
        db = web.database(dbn='mysql',db='blog',user='root')
        return 'open db'

iwuo_app = web.application(urls,locals())

