from django.contrib import admin
from .models import Categoria, Post #para poder trabajar con  clases las importo
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
    
    
admin.site.register(Categoria, CategoriaAdmin)#para registralo todo
admin.site.register(Post, PostAdmin)