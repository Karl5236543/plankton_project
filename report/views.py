from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from research_base.models import Sample, Cell, Cell_params, Station
from research_base.views import calculate

def sample_report_view(request, id):
    sample = Sample.objects.get(id=id)
    station = sample.station
    station_name, area_name = station.name, station.research.area_name
    cells = Cell.objects.filter(sample_id=id)
    for cell in cells:
        form = cell.form
        cell_params_dict_V = {p.name: p.value for p in Cell_params.objects.filter(cell=cell.id, formula='V')}
        cell_params_dict_P = {p.name: p.value for p in Cell_params.objects.filter(cell_id=cell.id, formula='P')}
        cell.V = calculate(form.formula_V, cell_params_dict_V)
        cell.P = calculate(form.formula_P, cell_params_dict_P)
    V = sum(cell.V for cell in cells)
    P = sum(cell.P for cell in cells)
    return render(request, 'report/sample_report.html', context={
        'sample': sample,
        'station': station,
        'station_name': station_name,
        'area_name': area_name,
        'cells': cells,
        'V': V,
        'P': P,
        'thead': Cell.get_thead()
    })


def sample_report_json_view(request, id):
    station_data = {
        "labels": [],
        "values": [],
        "background_colors": [],
        "boarder_colors": [],
    }
    sample = Sample.objects.get(id=id)
    types = set(cell.type.name for cell in Cell.objects.filter(sample_id=id))
    print(types)

    for type in types:
        station_data["values"].append(
            sum(cell.count for cell in Cell.objects.all() if cell.type.name == type))
    station_data["labels"] = list(types)
    station_data["background_colors"] = ["rgba(255, 99, 132, 0.2)"] * len(types)
    station_data["boarder_colors"] = ["rgb(255, 99, 132)"] * len(types)
    return JsonResponse(station_data)

