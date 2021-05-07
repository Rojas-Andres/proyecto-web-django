from django.shortcuts import render

# Create your views here.
def contacto(req):
    return render(req,"contacto/contacto.html")