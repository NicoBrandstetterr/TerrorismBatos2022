from django.http import HttpResponse
from django.shortcuts import render
from terrorismapp.models import gName

def seleccion_preguntas(request):
    return render(request,"principal.html")


def primeraQuery(request):
    #query=gName.objects.raw('SELECT * FROM Tabla WHERE gname = "Hutu extremists"')
    query=gName.objects.filter(gname='Hutu extremists')
    return render(request, "1query.html",{"Tabla":query})


def segundaQuery(request):
    query=gName.objects.raw('SELECT * FROM Tabla WHERE gname = "Hutu extremists"')
    #query=gName.objects.filter(gname='Hutu extremists')
    return render(request, "1query.html",{"Tabla":query})