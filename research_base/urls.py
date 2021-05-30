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

    path('cell_create', cell_create_view, name='cell_create'),
    path('cell_edit/<uuid:id>', cell_edit_view, name='cell_edit'),
    path('cell_delete/<uuid:id>', cell_delete_view, name='cell_delete'),

    path('get_form_params/<uuid:id>', get_form_params_view, name='get_form_params'),
    path('get_cell/<uuid:id>', get_cell_view, name='get_cell'),
    path('cell/<uuid:id>', cell_view, name='cell'),

    path('types/', types_viw, name='types'),
]