from django.urls import path
from .views import *

urlpatterns=[

    path('',list_project),
    path('create',create_project),
    path('<int:id>',project_details),
    path('<int:id>/update',update_project),
    path('<int:id>/delete',delete_project),

]