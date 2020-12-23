from django.db import models
from datetime import datetime, date, timedelta
from companies.models import Companies
from django.contrib.auth.models import User
from django.utils import timezone

class Process(models.Model):
    companie = models.ForeignKey(Companies, null=False, blank=False, on_delete=False,
        related_name='empresa_routine', verbose_name='Empresa')

    SISTEMOPERATIONCHOICES = (
    ('Linux', 'Linux'),
    ('Windows', 'Windows'),
    ('Outros', 'Outros'),
    )
    sistem_operation = models.CharField('S.O',max_length=20,
        choices=SISTEMOPERATIONCHOICES,blank=True, null=True, default='Linux')        

    user_create = models.ForeignKey(
        User, on_delete=False, null=True, blank=True, related_name='User_routine', verbose_name="Usuário")        
     
    date_create = models.DateField(
        'Atualizada', blank=True, null=True, default=timezone.now())
    
    date_update = models.DateField(
        'Emissão', blank=True, null=True, auto_now=True)

    title = models.CharField(
        'Título', max_length=80, blank=False,null=False)

    specification = models.TextField(
        'Processo', blank=False,null=False)

    def get_nickname_companie(self):
        return self.companie.nickname+' - '+self.machine_type
    get_nickname_companie.short_description = 'Empresa'

    class Meta:
        verbose_name = 'Rotina - Suporte'
        verbose_name_plural = 'Rotinas - Suporte'
        ordering = ['title']
