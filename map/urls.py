from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('stations_json', stations_json_view, name='stations_json'),
    path('research_stations_json/<uuid:id>', research_stations_json_view, name='research_stations_json'),
    path('station_json/<uuid:id>', station_json_view, name='station_json'),
    path('cell_data_json/<uuid:id>', cell_data_json_view, name='cell_data_json'),
]