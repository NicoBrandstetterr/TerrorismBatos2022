from django.http import HttpResponse
from django.shortcuts import render

def seleccion_preguntas(request):
    return render(request,"principal.html")

def Buscar(request):
    mensaje="Esta representa la tabla respuesta a la query %r" %request.GET["prd"]
    return HttpResponse(mensaje)