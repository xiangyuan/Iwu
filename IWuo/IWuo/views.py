#my first djang view
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello world welcome to here!')
