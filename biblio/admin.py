from django.contrib import admin
from biblio import models

# Register your models here.
admin.site.register(models.Autores)
admin.site.register(models.Editoriales)
admin.site.register(models.Libros)
admin.site.register(models.Sinopsis)
admin.site.register(models.Lectores)
admin.site.register(models.Prestamos)
admin.site.register(models.Devoluciones)
admin.site.register(models.Multas)