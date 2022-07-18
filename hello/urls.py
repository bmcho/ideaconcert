from django.urls import path
from hello.views import hello

app_name = 'hello'
urlpatterns = [
    path('hello', hello)
]
