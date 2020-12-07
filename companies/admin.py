from django.contrib import admin
from .models import Companies

class CompaniesAdmin(admin.ModelAdmin):
    # Campos que aparecerão ao entrar na model
    list_display = ('name', 'nickname', 'email','active',
                    'phone_one', 'phone_two', 'phone_three')

    # Campos que aparecerão ao entrar nos detalhes do model
    # Modo agrupado - Denomina um grupo de informações separada por um título
    fieldsets = (
        ('Situação da Empresa na Trabin', {
            'fields': (('active', 'create_add'),)}),
        ('Dados da Empresa', {
            'fields': (('name', 'nickname',), ('email', 'fundation'), ('cnpj', 'ie',))}),

        ('Dados do Proprietário',
            {'fields': (('owner', 'owner_phone'),)}),
        ('Endereço',
            {'fields': (('street', 'street_number'), ('district','city'), ('state', 'cep'))}),
        ('Telefones',
            {'fields': (('phone_one', 'phone_two',), ('phone_three'),)}),
        ('Observações',
            {'fields': (('observation',),)}),
    )
    # 2º Tipo 2 de pesquisa para tabelas relacionadas - Apresenta no modo lista e detalhado
    # autocomplete_fields = ("quotation_number",)

    # Desativa a edição do campo, e com isto ele pode ser usado na tela de detalhes
    # readonly_fields = ('',)

    # Executa uma ação quando em uma lista de dados - Tem que criar um arquivo action,py e colocar as defs dentro
    # actions = [check_email_contact]

    # Paginação para o listplay
    list_per_page = 50

    # Campos que unidos são usados no processo de filtragem por seleção
    list_filter = ('active','city',)

    # Campos que unidos são usados no processo de filtragem por digitação
    search_fields = ('name', 'nickname','phone_one',
                     'phone_two', 'phone_three',)

    # Se true, aparece um campo para salvar e duplicar
    save_as = True

    # Duplica os botões de salvar, apagar e editar em cima
    save_on_top = True

    # Força a informa o total de registros na tabela se false, mostra o texto "Mostrar Tudo"
    show_full_result_count = True

admin.site.register(Companies, CompaniesAdmin)

