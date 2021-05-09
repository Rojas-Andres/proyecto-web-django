from django.shortcuts import render,redirect 
from .carro import Carro
from tienda.models import Producto

# Create your views here.

def agregar_producto(req,producto_id):
    carro = Carro(req) #inicializamos carro
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto) #Agregamos el producto
    return redirect("tienda")

def eliminar_producto(req,producto_id):
    carro = Carro(req) #inicializamos carro
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto) #Agregamos el producto
    return redirect("tienda")

def restar_producto(req,producto_id):
    carro = Carro(req) #inicializamos carro
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto) #Agregamos el producto
    return redirect("tienda")
    
def limpiar_carro(req,producto_id):
    carro = Carro(req) #inicializamos carro
    carro.limpiar_carro()
    return redirect("tienda")