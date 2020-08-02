from django.urls import path
from django.conf.urls import include,url
from . import views
from django.conf.urls.static import static
from django.conf import settings

#ALL URLS FOR /PROPERTIES/
urlpatterns = [
   path("",views.index),
   path("new",views.new),
   path("edit",views.edit),
   path("update",views.update),
   path("create",views.create),
   path("delete",views.delete),
   path("change_list_status",views.change_list_status),
   path("view",views.view),
   path("approve",views.approve),
   path("disapprove",views.disapprove),

]
