# Este es el ursl de la aplicacion no del proyecto
from django.urls import path
from blog import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog,name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria,name="categoria")
]

