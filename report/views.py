from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from research_base.models import Cell

def cell_report_view(request, id):
    return render(request, 'report/cell_report.html')
