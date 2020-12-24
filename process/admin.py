from django.contrib import admin
from .models import Process

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('title','sistem_operation','specification',)


    # Paginação para o listplay
    list_per_page = 25

    # Campos que unidos são usados no processo de filtragem por seleção
    list_filter = ('title','specification',)

    # Campos que unidos são usados no processo de filtragem por digitação
    search_fields = ('title', 'specification',)

    # Se true, aparece um campo para salvar e duplicar
    save_as = True

    # Duplica os botões de salvar, apagar e editar em cima
    save_on_top = True

    # Força a informa o total de registros na tabela se false, mostra o texto "Mostrar Tudo"
    show_full_result_count = True

admin.site.register(Process,ProcessAdmin)    
