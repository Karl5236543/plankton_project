from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import View
from .models import *
import json


def get_stations_json(id=None):
    stations = {
        "type": "FeatureCollection",
        "features": []
    }
    station_list = Station.objects.filter(research_id=id) if id else Station.objects.all()
    for station in station_list:
        stations["features"].append({
            "type": "Feature",
            "properties": {
                "name": station.name,
                "depth": station.depth,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    station.coords["x"],
                    station.coords["y"]
                ]
            }
        })
    return stations


def index(request):
    return render(request, 'research_base/index.html')


#----------------------------------------------------------------------------------#
# Cell
#----------------------------------------------------------------------------------#
def sample_view(request, id):
    thead = ["время создания", "тип", "форма", "количество", "V", "P"]
    cells = Cell.objects.filter(sample_id=id)
    current_sample = Sample.objects.get(id=id)
    types = Type.objects.all()
    forms = Form.objects.all()
    return render(request, 'research_base/sample.html', context={
        'thead': thead,
        'cells': cells,
        'types': types,
        'forms': forms,
        'current_sample': current_sample,
    })

def cell_create_view(request):
    return redirect('/', permanent=False)


def cell_edit_view(request, id):
    return redirect('/', permanent=False)


def cell_delete_view(request, id):
    return redirect('/', permanent=False)


#----------------------------------------------------------------------------------#
# Sample
#----------------------------------------------------------------------------------#
def sample_create_view(request):
    horizont = request.POST.get('horizont')
    time = request.POST.get('time')
    station_id = request.POST.get('station_id')
    station=Station.objects.get(id=station_id)
    sample = Sample(horizont=horizont, time=time, station=station)
    sample.save()
    return redirect(station.get_absolute_url(), permanent=False)


def sample_edit_view(request, id):
    horizont = request.POST.get('horizont')
    time = request.POST.get('time')
    sample = Sample.objects.get(id=id)
    sample.horizont = horizont
    sample.time = time
    sample.save()
    station = Station.objects.get(id=sample.station_id)
    return redirect(station.get_absolute_url(), permanent=False)


def sample_delete_view(request, id):
    sample = Sample.objects.get(id=id)
    sample.delete()
    station = Station.objects.get(id=sample.station_id)
    return redirect(station.get_absolute_url(), permanent=False)


def Stations_view(request):
    stations = get_stations_json()
    return JsonResponse(stations)


def station_view(request, id):
    thead = ["время создания", "горизонт", "время сбора", "количество клеток"]
    samples = Sample.objects.filter(station_id=id)
    print(samples)
    current_station = Station.objects.get(id=id)
    return render(request, 'research_base/station.html', context={
        'thead': thead,
        'samples': samples, 
        'current_station': current_station,
    })


#----------------------------------------------------------------------------------#
# Station
#----------------------------------------------------------------------------------#
def station_create_view(request):
    name = request.POST.get('name')
    depth = request.POST.get('depth')
    date = request.POST.get('date')
    research_id = request.POST.get('research_id')
    research=Research.objects.get(id=research_id)
    station = Station(name=name, depth=depth, date=date, coords={'x':12312, 'y':6725}, research=research)
    station.save()
    return redirect(research.get_absolute_url(), permanent=False)


def station_edit_view(request, id):
    name = request.POST.get('name')
    depth = request.POST.get('depth')
    date = request.POST.get('date')
    station = Station.objects.get(id=id)
    station.name = name
    station.depth = depth
    station.date = date
    station.save()
    research = Research.objects.get(id=station.research_id)
    return redirect(research.get_absolute_url(), permanent=False)


def station_delete_view(request, id):
    station = Station.objects.get(id=id)
    station.delete()
    research = Research.objects.get(id=station.research_id)
    return redirect(research.get_absolute_url(), permanent=False)


def Stations_view(request):
    stations = get_stations_json()
    return JsonResponse(stations)



#----------------------------------------------------------------------------------#
# Research
#----------------------------------------------------------------------------------#
def research_list_view(request):
    thead = ["время создания", "название", "название района", "количество станций"]
    researches = Research.objects.all()
    return render(request, 'research_base/research_list.html', context={
        'thead': thead,
        'researches': researches,
    })


def research_view(request, id):
    thead = ["время создания", "название", "глубина", "время прибытия", "количество образцов"]
    stations = Station.objects.filter(research_id=id)
    current_research = Research.objects.get(id=id)
    return render(request, 'research_base/research.html', context={
        'thead': thead,
        'stations': stations ,
        'current_research': current_research,
        "page": "research",
    })


def research_create_view(request):
    research_name = request.POST.get('research_name')
    research_area_name = request.POST.get('research_area_name')
    Research.objects.create(name=research_name, area_name=research_area_name, area={'x':12312, 'y':6725})
    return redirect('research_list', permanent=False)


def research_edit_view(request, id):
    research_name = request.POST.get('research_name')
    research_area_name = request.POST.get('research_area_name')
    research = Research.objects.get(id=id)
    research.name = research_name
    research.area_name = research_area_name
    research.save()
    return redirect('research_list', permanent=False)


def research_delete_view(request, id):
    research = Research.objects.get(id=id)
    research.delete()
    return redirect('research_list', permanent=False)






