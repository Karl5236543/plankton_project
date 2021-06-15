from django.http.response import HttpResponse
from django.shortcuts import render

def type_list_view(request):
    return HttpResponse('types...')


def form_list_view(request):
    return HttpResponse('forms...')
