from django.shortcuts import render,redirect
from .forms import FormularioContacto

from django.core.mail import EmailMessage # Para enviar correos
from ProyectoWeb.settings import correo # Traemos el correo de la configuracion que lee el archivo .txt

# Create your views here.
def contacto(req):
    formulario_contacto = FormularioContacto() # Creamos una instancia de la clase
    if req.method=="POST":
        formulario_contacto = FormularioContacto(data=req.POST) # Rescatamos la data que el usuario ha enviado por el formulario el diccionario y le pasamos el constructor
        if formulario_contacto.is_valid():
            nombre = req.POST.get("nombre")
            correo_form = req.POST.get("email")
            contenido = req.POST.get("contenido")

            #print("\n\n correo",correo)
            email=EmailMessage("Mensaje desde App django",
            "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,correo_form,contenido),
            "",[correo],reply_to=[correo_form]
            )
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
            
    

    return render(req,"contacto/contacto.html",{"miFormulario":formulario_contacto})