import blog
import IWuo
import web

mapping = (('/blog',blog.urls,blog),
            ('/iwuo',iwuo.urls,iwuo)
        )

if __name__ == '__main__':
    delegate.run(mapping)
