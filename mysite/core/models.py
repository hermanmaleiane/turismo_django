from django.db import models

# Create your models here.

class PontoTuristico(models.Model):
    idPonto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000, blank=True, null=True)
    categoria = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return self.idPonto

    class Meta:
        ordering = ["idPonto"]
