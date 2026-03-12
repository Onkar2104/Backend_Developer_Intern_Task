from django.urls import path
from .views import *

urlpatterns=[

path('create',create_report),
path('<int:project_id>',list_reports)

]