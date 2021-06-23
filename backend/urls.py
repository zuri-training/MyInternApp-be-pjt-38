from django.urls import path, include

from .views import general as general_views

urlpatterns = [
    path("", general_views.home, name="home"),
]
