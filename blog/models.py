from django.db import models
from django.contrib.auth.models import User # Importamos los usuarios
# Create your models here.
class Categoria(models.Model):
    nombre    = models.CharField(max_length=50)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'categoria' # El nombre que va a tener en la base de datos 
        verbose_name_plural="categorias"    
    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo     = models.CharField(max_length=50)
    contenido  = models.CharField(max_length=50)
    imagen     = models.ImageField(upload_to='blog',null=True,blank=True) # Si no quiere introducir la imagen se puede quedar en blanco
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now_add=True)
    autor      = models.ForeignKey(User, on_delete=models.CASCADE) # Un autor puede tener multiples post
    categorias = models.ManyToManyField(Categoria) # DE MUCHOS A MUCHOS un post puede tener muchas categorias y una categoria puede tener multiples post
    class Meta:
        verbose_name = 'post' 
        verbose_name_plural="posts"
    
    def __str__(self):
        return "El titulo es {} ".format(self.titulo)

