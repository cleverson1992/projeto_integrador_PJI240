from django.contrib import admin
from .models import DadosProdutos, Localidades

# Register your models here.
admin.site.register(Localidades)
admin.site.register(DadosProdutos)