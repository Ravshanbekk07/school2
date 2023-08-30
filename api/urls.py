from django.urls import path
from .views import get_students,create

urlpatterns=[
    path('pupils/all',get_students),
    path('pupils/create',create),
]