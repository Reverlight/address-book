from django.urls import path

from .views import add_contact, contacts_list, edit_contact, delete_contact

urlpatterns = [
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:id>/', edit_contact, name='edit_contact'),
    path('delete/<int:id>/', delete_contact, name='delete_contact'),
    path('', contacts_list, name='contacts_list')
]

