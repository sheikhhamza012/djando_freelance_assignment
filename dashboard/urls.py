from django.urls import path
from django.conf.urls import include,url
from . import views
#URLS FOR /DASHBOARD/
urlpatterns = [
   path("",views.index),
   path("reviewer",views.reviewer),
   path("student",views.student),
   path("landlord",views.landlord),
   path("favorites",views.favorites),
  
]
