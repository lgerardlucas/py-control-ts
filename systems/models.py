from django.db import models
from django.utils import timezone

class Systems(models.Model):
    name = models.CharField(
        'Módulo', max_length=80, blank=False,null=False)

    description = models.TextField(
        'Descrição', blank=True, null=True)
    
    date_create = models.DateTimeField(
        'Atualizada', blank=True, null=True, default=timezone.now)
    
    date_update = models.DateField(
        'Emissão', blank=True, null=True, auto_now=True)


    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['name']

    def __str__(self):
        return self.name
