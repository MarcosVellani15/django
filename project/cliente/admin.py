from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Pais)
admin.site.register(models.clientes)
admin.site.register(models.compra)