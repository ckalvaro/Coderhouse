from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader

def inicio(request):
    return render(request, 'DesafioEntregable/inicio.html')

