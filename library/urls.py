from django.urls import path
from .views import *

urlpatterns = [
    path('type_list', type_list_view, name='type_list'),
    path('form_list', form_list_view, name='form_list'),
]