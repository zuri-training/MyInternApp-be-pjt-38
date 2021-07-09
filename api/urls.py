from django.conf.urls import url
from django.urls import path, include
from .aci import RegisterApi

urlpatterns = [
    path('aci/register', RegisterApi.as_view()),
]
