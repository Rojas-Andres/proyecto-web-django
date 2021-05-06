from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo    = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen    = models.ImageField(upload_to='servicios') # Los archivos subidos van a estar en media/servicios
    created   = models.DateTimeField(auto_now_add=True) # Agregar la fecha automaticamente
    updated   = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'servicio' # El nombre que va a tener en la base de datos 
        verbose_name_plural="servicios"
    
    def __str__(self):
        return "El titulo es {} ".format(self.titulo)
