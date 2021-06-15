from django.http.response import JsonResponse
from django.shortcuts import render
from django.conf import settings
import os
import json
from research_base.models import Station
from .utils import *

def stations_json_view(request):
    return JsonResponse(get_stations_json())

def research_stations_json_view(request, id):
    return JsonResponse(get_stations_json(res_id=id))

def station_json_view(request, id):
    return JsonResponse(get_stations_json(st_id=id))


def cell_data_json_view(request, id):
    date_start = request.GET.get("date_start")
    date_end = request.GET.get("date_end")
    return JsonResponse(get_cells_data_json(id, date_start, date_end))

