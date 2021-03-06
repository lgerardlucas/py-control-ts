from django.db import models
from companies.models import Companies
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class Bank(models.Model):
    """
    Model referente aos dados bancarios de todas as empresas 
    que geram remessa 
    """
    companie = models.ForeignKey(Companies, null=False, blank=False, on_delete=False,
        related_name='empresa_bank', verbose_name='Empresa')

    user_create = models.ForeignKey(
        User, on_delete=False, null=False, blank=False, related_name='user_bank', verbose_name="Usuário")

    MENUCHOICES = (
        ('Banco do Brasil - 001', 'Banco do Brasil - 001'),
        ('Banrisul - 041', 'Banrisul - 041'),
        ('CEF - 104', 'CEF - 104'),
        ('Itáu - 341', 'Itáu - 341'),
        ('Santander - 033', 'Santander - 033'),
        ('Sicredi - 748', 'Sicredi - 748'),
    )
    bank = models.CharField('Banco', max_length=100,
        choices=MENUCHOICES, blank=True, null=True, default='Outros')

    date_create = models.DateTimeField(
        'Cadastro', blank=True, null=True)

    enable_bank = models.BooleanField(
        'Ativo', blank=False, null=False, default=True)

    date_inactive = models.DateField(
        'Inativado', blank=True, null=True)


    cedante_code = models.CharField(
        'Cód/Cedente', max_length=50, blank=True, null=True)

    agency = models.CharField(
        'Agência', max_length=10, blank=True, null=True)
    
    account = models.CharField(
        'Conta Corrente',max_length=50, blank=True, null=True)

    date_update = models.DateTimeField(
        'Últ/Verificação', blank=True, null=True, default=timezone.now)

    def get_nickname_companie_bank(self):
        return self.companie.nickname
    get_nickname_companie_bank.short_description = 'Empresa'

    def get_user_bank(self):
        return self.user_create.username.capitalize()
    get_user_bank.short_description = 'Usuário'

    class Meta:
        verbose_name = 'Remessa Bancária'
        verbose_name_plural = 'Remessas Bancárias'
        ordering = ['companie__nickname','bank']

    def __str__(self):
        return self.companie.nickname+' '+self.bank
