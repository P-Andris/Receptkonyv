from django.db import models
from django.shortcuts import get_object_or_404

class Kategoria(models.Model):
    nev = models.CharField(max_length = 15, verbose_name = 'Név')

    def __str__(self):
        return self.nev
    
class Recept(models.Model):
    nev = models.CharField(max_length = 60, verbose_name = 'Név')
    kat_id = models.ForeignKey(Kategoria, on_delete = models.CASCADE, verbose_name = 'Kategória')
    leiras = models.TextField(verbose_name = 'Leírás')
    kep_eleresi_ut = models.CharField(max_length = 255, verbose_name = 'Kép URL')
    hirdetes_datuma = models.DateField(null = True, blank = True, verbose_name = 'Hirdetés dátuma')

    def __str__(self):
        return self.nev