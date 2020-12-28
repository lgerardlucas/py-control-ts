from django.db import models
from datetime import date


class Companies(models.Model):
    """
    Model referente as empresas a serem tratadas por este sistema em diversas 
    processos diferentes
    """
    name = models.CharField(
        'Empresa', max_length=200, null=False, blank=False,db_index=True)
    nickname = models.CharField(
        'Apelido', max_length=50, null=False, blank=False,db_index=True)
    owner = models.CharField(
        'Proprietário', max_length=100,null=False, blank=False,)
    owner_phone = models.CharField(
        'Fone Proprietário', max_length=20, blank=False, null=False)
    create_add = models.DateField(
        'Cadastro', blank=False, null=False, default=date.today)
    fundation = models.DateField(
        'Fundação', blank=True,null=True)
    phone_one = models.CharField(
        'Fone 1', max_length=20, blank=False, null=False)
    phone_two = models.CharField(
        'Fone 2', max_length=20, blank=False, null=False)
    phone_three = models.CharField(
        'Fone 3', max_length=20, blank=False, null=False)
    cnpj = models.CharField(
        'CNPJ', max_length=20, blank=False, null=False)
    ie = models.CharField(
        'IE', max_length=20, blank=False, null=False)
    email = models.EmailField(
        'E-mail', blank=True,null=True)
    active = models.BooleanField(
        'Ativo(S/N)', blank=True, default=True)
    observation = models.TextField(
        'Observações',blank=True)
    street = models.CharField(
        'Endereço', max_length=150, blank=False,null=False)
    street_number = models.CharField(
        'Complemento', max_length=20, blank=True,null=True)
    state = models.CharField(
        'Estado', max_length=2, blank=False,null=True)
    district = models.CharField(
        'Bairro', max_length=50,blank=False,null=False)
    city = models.CharField(
        'Cidade',max_length=50,blank=False,null=False)
    cep = models.CharField( 
        'Cep',max_length=9,blank=False,null=False)
    id_old = models.IntegerField(
        'ID Sistem Antigo',blank=True,null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['name']

    def __str__(self):
        return self.name

