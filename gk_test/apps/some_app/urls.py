from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.some_app, name='some_app'),
]