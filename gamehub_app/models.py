from django.db import models

class FelaDaPuta(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
