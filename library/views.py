from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from research_base.models import Type, Form



def type_list_view(request):
    types = Type.objects.all()
    return render(request, 'library/type_list.html', context={
        'types': types
    })


def create_type_view(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    Type.objects.create(name=name, description=description)
    return redirect('type_list', permanent=False)


def edit_type_view(request, id):
    name = request.POST.get("name")
    description = request.POST.get("description")
    cell_type = Type.objects.get(id=id)
    cell_type.description = description
    cell_type.name = name
    cell_type.save()
    return redirect('type_list', permanent=False)


def delete_type_view(request, id):
    Type.objects.get(id=id).delete()
    return redirect('type_list', permanent=False)


def form_list_view(request):
    return HttpResponse('forms...')
