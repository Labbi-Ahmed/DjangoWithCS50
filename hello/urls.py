

from importlib.resources import path
from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index, name="index"),
    path("<str:name>", views.randf, name="rendf"),
    path("labib", views.labib, name="labib"),
    path("joty", views.joty, name="joty")
]