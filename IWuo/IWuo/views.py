#my first djang view
from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse('Hello world')
# current system time
def mytime(request):
    now = datetime.now()
    html = '<html><body>The time now %s</body></html>'% now
    return HttpResponse(html)
