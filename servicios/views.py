from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(req):
    servicios = Servicio.objects.all() # Traiga todos los servicios que esten creados

    return render(req,"servicios/servicios.html",{"servicios":servicios})
