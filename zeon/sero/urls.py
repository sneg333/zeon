from django.conf.urls import url
from . import views

urlpatterns = [

    url("sero", views.sero, name='sero'),

]