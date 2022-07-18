from django.urls import path

from api.views   import HelloApiView

urlpatterns = [
    path('/hello', HelloApiView.as_view()),
]