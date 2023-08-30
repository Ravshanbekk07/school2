from django.urls import path
from .views import (get_students,
                    create,get_id,update,delete,
                    get_contact,contact_id,create_contact,
                    update_contact,delete_contact)

urlpatterns=[
    path('pupils/all',get_students),
    path('pupils/create',create),
    path('pupils/<int:pk>',get_id),
    path('pupils/<int:pk>/update',update),
    path('pupils/<int:pk>/delete',delete),

    
    path('contact/all',get_contact),
    path('contact/<int:pk>/getcontact',contact_id),
    path('contact/createcontact',create_contact),
    path('contact/<int:pk>/updatecontact',update_contact),
    path('contact/<int:pk>/deletecontact',delete_contact),
]