from django.db import models
from datetime import datetime, date, timedelta
from companies.models import Companies
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils import timezone

class Servers(models.Model):
    """
    Dados referente a cada servidor de uma empresa, tendo como informacao,
    dados como: processador, memoria, tipo de so e senhas...
    """
    companie = models.ForeignKey(Companies, null=False, blank=False, on_delete=False,
        related_name='empresa_server', verbose_name='Empresa')

    processor = models.CharField(
        'Processador',max_length=150, null=True,blank=True)

    memory_ram = models.CharField(
        'RAM(GB)', max_length=20, null=True,blank=True)
    
    memory_ram_initials = models.CharField(max_length=2,
        blank=True, null=True, default='GB')

    ip_network = models.CharField(
        'IP', max_length=20, null=True, blank=True)

    virtual_machine = models.BooleanField(
        'Máquina Virtual(S/N)', null=True,blank=True, default=False)
    
    SISTEMOPERATIONCHOICES = (
    ('Linux', 'Linux'),
    ('Windows', 'Windows'),
    ('Outros', 'Outros'),
    )
    sistem_operation = models.CharField('S.O',max_length=20,
        choices=SISTEMOPERATIONCHOICES,blank=True, null=True, default='Linux')        

    MACHINETYPECHOICES = (
        ('Produção', 'Produção'),
        ('Contingência', 'Contingência'),
        ('Outros', 'Outros'),
    )
    machine_type = models.CharField('Tipo de Máquina', max_length=20,
        choices=MACHINETYPECHOICES,blank=False, null=False, default='Produção')

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

    date_acquisition = models.DateField(
        'Data de Compra', blank=True, null=True)

    provider_acquisition = models.CharField(
        'Fornecedor do Equipamento', max_length=150, null=True, blank=True)

    last_verification = models.DateField(
        'Última Verificação', blank=True, null=True, default=timezone.now)

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
            self.user_verification.username.capitalize(),
       )
    validate_verification.short_description = 'Última Verificação'

    def get_nickname_companie(self):
        return self.companie.nickname+' - '+self.machine_type
    get_nickname_companie.short_description = 'Empresa'

    def get_memory_ram_initial(self):
        return self.memory_ram+'GB'
    get_memory_ram_initial.short_description = 'RAM(GB)'

    class Meta:
        verbose_name = 'Servidor - Cadastro'
        verbose_name_plural = 'Servidores - Cadastros'
        ordering = ['companie__nickname', 'machine_type','ip_network']


    def __str__(self):
        return self.companie.nickname+' '+self.ip_network+' '+self.machine_type


class Information(models.Model):
    server = models.ForeignKey(Servers, null=False, blank=False, on_delete=True,
        related_name='server_info', verbose_name='Servidor')

    database_name = models.CharField(
        'Name do Banco', max_length=50, blank=True, null=True,default='.')

    database_size = models.FloatField(
        'Tamanho do Banco', blank=True, null=True)

    DATABASESIZEINITIALCHOICES = (
        ('MB', 'MB'),
        ('GB', 'GB'),
        ('TB', 'TB'),
    )
    database_size_initials = models.CharField(max_length=2,
        choices=DATABASESIZEINITIALCHOICES,blank=True, null=True, default='GB')

    hd_size_one = models.FloatField(
        'Tam/Disco(SO)', blank=True, null=True)
    hd_size_one_initials = models.CharField(max_length=2,
        blank=True, null=True, default='GB')

    hd_size_one_available = models.FloatField(
        'Tam/Disco Disp(SO)', blank=True, null=True)
    hd_size_one_available_initials = models.CharField(max_length=2,
        blank=True, null=True, default='GB')

    hd_size_two = models.FloatField(
        'Tam. Disco(BD)', blank=True, null=True)
    hd_size_two_initials = models.CharField(max_length=2,
        blank=True, null=True, default='GB')

    hd_size_two_available = models.FloatField(
        'Tam/Disc Disp(BD)', blank=True, null=True)
    hd_size_two_available_initials = models.CharField(max_length=2,
        blank=True, null=True,default='GB')

    last_verification = models.DateField(
        'Última Verificação', blank=True, null=True,default=timezone.now)

    user_verification = models.ForeignKey(
        User, on_delete=False, null=False, blank=False, related_name='user_information', verbose_name="Usuário")

    def get_server_nickname_companie(self):
        return self.server.companie.nickname+' '+self.server.ip_network+' '+self.server.machine_type
    get_server_nickname_companie.short_description = 'Empresa'


    def verification_data(self):
        return format_html(
            '<span style="color: {};">{} - {} </span>',
            'black',
            self.last_verification.strftime('%d/%m/%Y'),
            self.user_verification.username.capitalize(),
        )
    verification_data.short_description = 'Última Verificação'

    def get_database_size_database_size_initials(self):
        if self.database_size:
            return format_html(
                '<span style="color: {}; width: 10px;">{} </span>',
                'black',
                str(self.database_size)+self.database_size_initials
            )
        else:
            return '.'
    get_database_size_database_size_initials.short_description = 'Tam(BD)'

    def get_hd_size_one_hd_size_one_initials(self):
        if self.hd_size_one:
            return format_html(
                '<span style="color: {};">{} </span>',
                'Maroon',
                str(self.hd_size_one)+self.hd_size_one_initials
            )
        else:
            return '.'
    get_hd_size_one_hd_size_one_initials.short_description = 'Tam/Disco(SO)'

    def get_hd_size_one_available_hd_size_one_available_initials(self):
        if self.hd_size_one_available:
            return format_html(
                '<span style="color: {};">{} </span>',
                'Maroon',
                str(self.hd_size_one_available)+self.hd_size_one_available_initials
            )
        else:
            return '.'
    get_hd_size_one_available_hd_size_one_available_initials.short_description = 'Tam/Disco Disp(SO)'

    def get_hd_size_two_hd_size_two_initials(self):
        if self.hd_size_two:
            return format_html(
                '<span style="color: {};">{} </span>',
                'DarkGreen',
                str(self.hd_size_two)+self.hd_size_two_initials
            )
        else:
            return '.'
    get_hd_size_two_hd_size_two_initials.short_description = 'Tam. Disco(BD)'

    def get_hd_size_two_available_hd_size_two_available_initials(self):
        if self.hd_size_two_available:
            return format_html(
                '<span style="color: {};">{} </span>',
                'DarkGreen',
                str(self.hd_size_two_available)+self.hd_size_two_available_initials
            )
        else:
            return '.'
    get_hd_size_two_available_hd_size_two_available_initials.short_description = 'Tam/Disc Disp(BD)'

    def get_sistem_operation(self):
        return self.server.sistem_operation
    get_sistem_operation.short_description = 'S.O'

    class Meta:
        verbose_name = 'Servidor - Informações'
        verbose_name_plural = 'Servidores - Informações'
        ordering = ['server__servers__companie__nickname',
                    'server__servers__machine_type',
                    'server__servers__ip_network',
                    '-last_verification']

    def __str__(self):
        return self.database_name
