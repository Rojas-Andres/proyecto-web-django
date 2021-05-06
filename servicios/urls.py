# Este es el ursl de la aplicacion no del proyecto
from django.urls import path
from servicios import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios,name="Servicios"),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Le agregamos la ruta para que cuando entremos a mirarla se encuentre la img