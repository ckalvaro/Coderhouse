from django.shortcuts import render
from django.db import models
from FamiliApp.models import Familiar
from django.template import Template, loader
from django.http import HttpResponse
# Create your views here.

def familiapp_inicio(request):
    familiar1 = Familiar(nombre = "Jorge", apellido="Rojas", edad=50, ultimo_asado = "01/01/2000")
    familiar1.save()
    familiar2 = Familiar(nombre = "Marcelo", apellido="Miraglia", edad=57, ultimo_asado = "17/05/2017")
    familiar2.save()
    familiar3 = Familiar(nombre = "Juan", apellido="Moreira", edad=37, ultimo_asado = "24/02/1995")
    familiar3.save()
    diccionario = {
        "f1nombre": familiar1.nombre, "f1apellido":familiar1.apellido, "f1edad":familiar1.edad, "f1ultimo_asado":familiar1.ultimo_asado,
        "f2nombre": familiar2.nombre, "f2apellido":familiar2.apellido, "f2edad":familiar2.edad, "f2ultimo_asado":familiar2.ultimo_asado,
        "f3nombre": familiar3.nombre, "f3apellido":familiar3.apellido, "f3edad":familiar1.edad, "f3ultimo_asado":familiar3.ultimo_asado
    }
    plantilla = loader.get_template('FamiliApp/familiapp_inicio.html')
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)

