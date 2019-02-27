from django.db import models

class Protheus(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    descricao = models.CharField(max_length=100)
