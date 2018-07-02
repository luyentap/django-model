from django.conf.urls import url, include
from .views import *
from . import views


urlpatterns = [
    url('home',views.formp,name="home"),
    url('list',ListProduct.as_view(),name="home"),
]
