from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Localidades(models.Model):
    localidade = models.CharField(max_length=100)

    def __str__(self):
        return self.localidade


class DadosProdutos(models.Model):
    produto = models.CharField(max_length=30)
    modelo = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    localidade = models.ForeignKey(Localidades, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.user.username