from django.urls import path
from django.conf.urls import include,url
from . import views

#FOR '/COMMENTS/'
urlpatterns = [
   path("",views.create),
]
