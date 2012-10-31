import web
import types



def delegate_apps(mappings):
    def f():
        for prefix,urls,fvars in mappings:
            if type(fvars) == types.MethodType:
                fvars = fvars.__dict__

            if web.ctx.path.startwith(prefix):
                path = web.ctx.path[len(prefix):]
                print path
                web.ctx.path = path
                return web.request.handle(urls,fvars,path)
         else:
             return web.NotFound()

         return f
    

def run(mapping):
    '''the mulity app delegate handle'''
    handler = delegate_apps(mapping)
    web.run(handler,{})
