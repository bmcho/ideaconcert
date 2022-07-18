from django.http import HttpResponse

def hellow_world(req):
    return HttpResponse('Hello world!')

