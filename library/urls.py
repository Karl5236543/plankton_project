from django.urls import path
from .views import *

urlpatterns = [
    path('type_list', type_list_view, name='type_list'),
    path('form_list', form_list_view, name='form_list'),
    path('create_type', create_type_view, name='create_type'),
    path('delete_type/<uuid:id>', delete_type_view, name='delete_type'),
    path('edit_type/<uuid:id>', edit_type_view, name='edit_type'),
]