from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('research_list', research_list_view, name='research_list'),

    path('research/<uuid:id>/', research_view, name='research'),
    path('research_create/', research_create_view, name='research_create'),
    path('research_delete/<uuid:id>/', research_delete_view, name='research_delete'),
    path('research_edit/<uuid:id>', research_edit_view, name='research_edit'),

    path('station/<uuid:id>/', station_view, name='station'),
    path('station_create/', station_create_view, name='station_create'),
    path('station_delete/<uuid:id>/', station_delete_view, name='station_delete'),
    path('station_edit/<uuid:id>', station_edit_view, name='station_edit'),

    path('sample/<uuid:id>/', sample_view, name='sample'),
    path('sample_create/', sample_create_view, name='sample_create'),
    path('sample_delete/<uuid:id>/', sample_delete_view, name='sample_delete'),
    path('sample_edit/<uuid:id>', sample_edit_view, name='sample_edit'),
]