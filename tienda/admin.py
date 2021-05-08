from django.contrib import admin
from tienda.models import Producto,CategoriaProd
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class CategoriaProddmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Producto,ProductoAdmin)
admin.site.register(CategoriaProd,CategoriaProddmin)