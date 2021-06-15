from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('sample_report/<uuid:id>/', sample_report_view, name='sample_report'),
    path('sample_report_json/<uuid:id>/', sample_report_json_view, name='sample_report_json'),
]