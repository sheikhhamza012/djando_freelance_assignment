from django.urls import path
from django.conf.urls import include,url
from . import views
urlpatterns = [
   path("",views.login),
   path("users/create",views.create),
   path("register",views.new),
   path("session",views.create_session),
   path("logout",views.logout)
]
