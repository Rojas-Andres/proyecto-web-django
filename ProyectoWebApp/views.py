from django.shortcuts import render,HttpResponse
from servicios.models import Servicio
# Create your views here.
def home(req):
    return render(req,"ProyectoWebApp/home.html")

def servicios(req):
    servicios = Servicio.objects.all() # Traiga todos los servicios que esten creados

    return render(req,"ProyectoWebApp/servicios.html",{"servicios":servicios})

def tienda(req):
    return render(req,"ProyectoWebApp/tienda.html")

def blog(req):
    return render(req,"ProyectoWebApp/blog.html")

def contacto(req):
    return render(req,"ProyectoWebApp/contacto.html")