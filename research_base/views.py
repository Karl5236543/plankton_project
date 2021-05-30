from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.conf import settings
from .models import *
from .utils import *


def index(request):
    return render(request, 'research_base/index.html')


def get_form_params_view(request, id):
    params_V = Form.objects.get(id=id).parameters_V.split(',')
    params_P = Form.objects.get(id=id).parameters_P.split(',')
    return JsonResponse({'params_V': list(params_V), 'params_P': list(params_P)})

def get_cell_view(request, id):
    cell = Cell.objects.get(id=id)
    cell_params_V = [{"name": p.name, "value": p.value} for p in Cell_params.objects.filter(cell_id=id, formula='V')]
    cell_params_P = [{"name": p.name, "value": p.value} for p in Cell_params.objects.filter(cell_id=id, formula='P')]
    cell_data = {
        'type': cell.type.name,
        "form": cell.form.name,
        "params_V": cell_params_V,
        "params_P": cell_params_P,
    }
    return JsonResponse(cell_data)


def cell_view(request, id):
    cells_type_data = []
    types = Type.objects.all()
    for type in types:
        cells_type_data.append(
            Cells_type_data(type.name, sum([cell.count for cell in Cell.objects.filter(type_id=type.id)] + [0]), type.id))

    cell = Cell.objects.get(id=id)
    if 'type_id' in request.GET:
        type_id = Type.objects.get(id=request.GET.get('type_id')).id
    else:
        type_id = cell.type_id

    form = cell.form
    cell_params_dict_V = {p.name: p.value for p in Cell_params.objects.filter(cell=cell.id, formula='V')}
    cell_params_dict_P = {p.name: p.value for p in Cell_params.objects.filter(cell_id=cell.id, formula='P')}
    cell.V = calculate(form.formula_V, cell_params_dict_V)
    cell.P = calculate(form.formula_P, cell_params_dict_P)

    cell_params_V = [(p.name, p.value) for p in Cell_params.objects.filter(cell_id=id, formula='V')]
    cell_params_P = [(p.name, p.value) for p in Cell_params.objects.filter(cell_id=id, formula='P')]
    return render(request, 'research_base/cell.html',context={
        'cell': cell,
        'cells_type_data': cells_type_data,
        'type_id': type_id,
        "cell_params_V": cell_params_V,
        "cell_params_P": cell_params_P,
    })
#----------------------------------------------------------------------------------#
# Cell
#----------------------------------------------------------------------------------#
def sample_view(request, id):
    
    cells = Cell.objects.filter(sample_id=id)
    for cell in cells:
        form = cell.form
        cell_params_V = {p.name: p.value for p in Cell_params.objects.filter(cell=cell.id, formula='V')}
        cell_params_P = {p.name: p.value for p in Cell_params.objects.filter(cell_id=cell.id, formula='P')}
        cell.V = calculate(form.formula_V, cell_params_V)
        cell.P = calculate(form.formula_P, cell_params_P)

    current_sample = Sample.objects.get(id=id)
    types = Type.objects.all()
    forms = Form.objects.all()
    return render(request, 'research_base/sample.html', context={
        'cells': cells,
        'types': types,
        'forms': forms,
        'current_sample': current_sample,
        'thead': Cell.get_thead(),
    })

def cell_create_view(request):
    form_id = request.POST.get('cell_form')
    type_id = request.POST.get('type')
    cell_count = request.POST.get('cell_count')
    cell_form = Form.objects.get(id=form_id)
    cell_type = Type.objects.get(id=type_id)

    sample_id = request.POST.get('sample_id')
    sample=Sample.objects.get(id=sample_id)

    new_cell = Cell(sample=sample, type=cell_type, form=cell_form, count=cell_count)
    new_cell.save()
    for param in cell_form.get_parameters_V():
        Cell_params.objects.create(cell=new_cell, name=param, value=request.POST.get('V_' + param), formula='V')
    for param in cell_form.get_parameters_P():
        Cell_params.objects.create(cell=new_cell, name=param, value=request.POST.get('P_' + param), formula='P')

    return redirect(sample.get_absolute_url(), permanent=False)


def cell_edit_view(request, id):
    cell = Cell.objects.get(id=id)
    station = Sample.objects.get(id=cell.sample_id)
    cell.type = Type.objects.get(id=request.POST.get('type'))
    cell.form = Form.objects.get(id=request.POST.get('cell_form'))
    cell.count = request.POST.get('cell_count')
    cell.save()
    for parameter in Cell_params.objects.filter(cell_id=id, formula='V'):
        parameter.value = request.POST.get('V_' + parameter.name)
        parameter.save()

    for parameter in Cell_params.objects.filter(cell_id=id, formula='P'):
        parameter.value = request.POST.get('P_' + parameter.name)
        parameter.save()

    return redirect(station.get_absolute_url(), permanent=False)


def cell_delete_view(request, id):
    cell = Cell.objects.get(id=id)
    station = Sample.objects.get(id=cell.sample_id)
    cell.delete()
    return redirect(station.get_absolute_url(), permanent=False)


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
    station = Station.objects.get(id=sample.station_id)
    sample.delete()
    return redirect(station.get_absolute_url(), permanent=False)


def station_view(request, id):
    try:
        title = request.GET.get('search_parameter')
    except KeyError:
        pass
    try:
        value = request.GET.get('search_name')
    except KeyError:
        pass
    
    if (title and value):
        field = Sample.get_field_name(title)
        filter_params = {
            'station_id' : id,
            field: request.GET.get('search_name')
        }
        samples = Sample.objects.filter(**filter_params)
    else:
        samples = Sample.objects.filter(station_id=id)
    current_station = Station.objects.get(id=id)
    
    return render(request, 'research_base/station.html', context={
        'samples': samples, 
        'current_station': current_station,
        'thead': Sample.get_thead(),
        "search_name": value,
        "search_parameter": title,
    })


#----------------------------------------------------------------------------------#
# Station
#----------------------------------------------------------------------------------#
def station_create_view(request):
    name = request.POST.get('name')
    depth = request.POST.get('depth')
    date = request.POST.get('date')
    coords = float(request.POST.get('lng')), float(request.POST.get('lat'))
    research_id = request.POST.get('research_id')
    research=Research.objects.get(id=research_id)
    station = Station(name=name, depth=depth, date=date, coords=coords, research=research)
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
    research = Research.objects.get(id=station.research_id)
    station.delete()
    return redirect(research.get_absolute_url(), permanent=False)

#----------------------------------------------------------------------------------#
# Research
#----------------------------------------------------------------------------------#
def research_list_view(request):
    try:
        title = request.GET.get('search_parameter')
    except KeyError:
        pass
    try:
        value = request.GET.get('search_name')
    except KeyError:
        pass
    
    if (title and value):
        field = Research.get_field_name(title)
        filter_params = {field: request.GET.get('search_name')}
        researches = Research.objects.filter(**filter_params)
    else:
        researches = Research.objects.all()
    return render(request, 'research_base/research_list.html', context={
        'thead': Research.get_thead(),
        'researches': researches,
        "search_name": value,
        "search_parameter": title,
    })


def research_view(request, id):
    try:
        title = request.GET.get('search_parameter')
    except KeyError:
        pass
    try:
        value = request.GET.get('search_name')
    except KeyError:
        pass
    
    if (title and value):
        field = Station.get_field_name(title)
        filter_params = {
            'research_id' : id,
            field: request.GET.get('search_name')
        }
        stations = Station.objects.filter(**filter_params)
    else:
        stations = Station.objects.filter(research_id=id)
        
    current_research = Research.objects.get(id=id)
    return render(request, 'research_base/research.html', context={
        'stations': stations ,
        'current_research': current_research,
        "page": "research",
        'thead': Station.get_thead(),
        "search_name": value,
        "search_parameter": title,
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




#----------------------------------------------------------------------------------#
# Calculations
#----------------------------------------------------------------------------------#

