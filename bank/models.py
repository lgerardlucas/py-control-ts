from django.db import models
from companies.models import Companies
from datetime import date
from django.utils import timezone

class Bank(models.Model):
    """
    Model referente aos dados bancarios de todas as empresas 
    que geram remessa 
    """
    companie = models.ForeignKey(Companies, null=False, blank=False, on_delete=False,
        related_name='empresa_bank', verbose_name='Empresa')

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

    enable_bank = models.BooleanField(
        'Ativo', blank=False, null=False,default=True)        

    date_update = models.DateField(
        'Cadastro', blank=True, null=True)

    date_create = models.DateTimeField(
        'Últ/Verificação', blank=True, null=True, default=timezone.now)

    cedante_code = models.CharField(
        'Cód/Cedente', max_length=50, blank=True, null=True)

    agency = models.CharField(
        'Agência', max_length=10, blank=True, null=True)
    
    account = models.CharField(
        'Conta Corrente',max_length=50, blank=True, null=True)

    def get_nickname_companie_bank(self):
        return self.companie.nickname
    get_nickname_companie_bank.short_description = 'Empresa'

    class Meta:
        verbose_name = 'Remessa Bancária'
        verbose_name_plural = 'Remessas Bancárias'
        ordering = ['companie__nickname','bank']

    def __str__(self):
        return self.companie.nickname+' '+self.bank
