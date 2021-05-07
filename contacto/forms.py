from django import forms

#Formulario de contacto
class FormularioContacto(forms.Form):
    nombre    = forms.CharField(label="Nombre",required=True)
    email     = forms.CharField(label="Email",required=True)
    contenido = forms.CharField(label="Contenido",widget=forms.Textarea)