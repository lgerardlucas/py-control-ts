from django.contrib import admin
from .models import Bank

class BankAdmin(admin.ModelAdmin):
    """
    Lista de campos para o administrador
    """
    # Campos que aparecerão ao entrar na model
    list_display = ('get_nickname_companie_bank', 'bank', 'enable_bank', 'date_inactive', 'date_update',
                    'date_create', 'cedante_code', 'agency', 'account', 'get_user_bank',)

    # Paginação para o listplay
    list_per_page = 50

    # Campos que unidos são usados no processo de filtragem por seleção
    list_filter = ('companie__nickname', 'bank',)

    # Campos que unidos são usados no processo de filtragem por digitação
    search_fields = ('bank', 'companie__nickname',)

    # Se true, aparece um campo para salvar e duplicar
    save_as = True

    # Duplica os botões de salvar, apagar e editar em cima
    save_on_top = True

    # Força a informa o total de registros na tabela se false, mostra o texto "Mostrar Tudo"
    show_full_result_count = True

    # Campos que serão links para acesso a model
    list_display_links = ('get_nickname_companie_bank','bank',)

admin.site.register(Bank, BankAdmin)
