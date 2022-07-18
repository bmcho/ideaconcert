
from django.contrib import admin
from django.urls import path, include
from ideaconcert.views import hellow_world

from ideaconcert.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/hello', hellow_world)
]
