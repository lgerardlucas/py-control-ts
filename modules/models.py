from django.db import models
from django.utils import timezone
from systems.models import Systems

class Modules(models.Model):
    system = models.ForeignKey(Systems, null=False, blank=False, on_delete=False,
        related_name='system_module', verbose_name='Sistema')

    MENUCHOICES = (
    ('Cadastros', 'Cadastros'),
    ('Movimentos', 'Movimentos'),
    ('Consultas', 'Consultas'),
    ('Relatórios', 'Relatórios'),
    ('Ferramentas', 'Ferramentas'),
    ('Outros', 'Outros'),
    )
    menu = models.CharField('Menu',max_length=20,
        choices=MENUCHOICES,blank=True, null=True, default='Outros')        

    name = models.CharField(
        'Módulo', max_length=80, blank=False,null=False,db_index=True)

    description = models.TextField(
        'Descrição', blank=True, null=True)
    
    date_create = models.DateTimeField(
        'Atualizada', blank=True, null=True, default=timezone.now)
    
    date_update = models.DateField(
        'Emissão', blank=True, null=True, auto_now=True)


    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['name','menu','system']

    def __str__(self):
        return str(self.name)
