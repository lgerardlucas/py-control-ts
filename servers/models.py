from django.db import models
from datetime import datetime, date, timedelta
from companies.models import Companies
from django.contrib.auth.models import User
from django.utils.html import format_html

class Servers(models.Model):
    companie = models.ForeignKey(Companies, null=False, blank=False, on_delete=False,
        related_name='empresa_server', verbose_name='Empresa')

    processor = models.CharField(
        'Processador',max_length=150, null=True,blank=True)

    memory_ram = models.CharField(
        'RAM', max_length=20, null=True,blank=True)
    
    ip_network = models.CharField(
        'IP', max_length=20, null=True, blank=True)
    
    SISTEMOPERATIONCHOICES = (
    ('Linux', 'Linux'),
    ('Windows', 'Windows'),
    ('Outros', 'Outros'),
    )
    sistem_operation = models.CharField('S.O',max_length=20,
        choices=SISTEMOPERATIONCHOICES,blank=True, null=True, default='Linux')        

    sistem_specification = models.CharField(
        'Especificação(S.O)', max_length=50, null=True, blank=True)

    user_sistem_operation = models.CharField(
        'Usuário(S.O)', max_length=50, null=True, blank=True)

    passwd_sistem_operation = models.CharField(
        'Senha(S.O)', max_length=50, null=True, blank=True) 
    
    partition_size_specification  = models.CharField(
        'Partições/Tamanho', max_length=50, null=True, blank=True) 

    DATABASEDEFINITIONCHOICES = (
    ('PosgreSQL', 'PostgreSQL'),
    ('Outros', 'Outros'),
    )
    database_definition = models.CharField('Banco de Dados',max_length=20,
        choices=DATABASEDEFINITIONCHOICES,blank=True, null=True, default='PostgreSQL')        

    database_version = models.CharField(
        'Versão', max_length=5, null=True, blank=True) 

    last_verification = models.DateField(
        'Última Verificação', blank=True,null=True)

    user_verification = models.ForeignKey(
        User, on_delete=False, null=True, blank=True, related_name='User', verbose_name="Usuário")        


    def validate_verification(self):
        if self.last_verification < date.today()+timedelta(days=30):
            color_alert = 'black'
        else:
            color_alert = 'red'
        return format_html(
            '<span style="color: {};">{} - {} </span>',
            color_alert,
            self.last_verification.strftime('%d/%m/%Y'),
            self.user_verification.username.upper(),
       )
    validate_verification.short_description = 'Última Verificação'


    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return self.companie.name
