from django.http import HttpResponse

def index(req):
    return HttpResponse('index페이지입니다.')

def hellow_world(req):
    return HttpResponse('Hello world!')