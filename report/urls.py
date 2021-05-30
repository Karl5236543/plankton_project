from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('cell_report/<uuid:id>/', cell_report_view, name='cell_report'),
]