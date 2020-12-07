from django.contrib import admin
from .models import Servers

class ServersAdmin(admin.ModelAdmin):
    list_display = ('companie', 'ip_network','sistem_operation','sistem_specification',
                    'memory_ram', 'partition_size_specification', 'database_definition', 'database_version', 'validate_verification')
    fieldsets = (
        ('Empresa Proprietária', {
            'fields': (('companie',),)}),

        ('Especificação do Servidor', {
            'fields': (('processor'), ('memory_ram', 'ip_network'), ('partition_size_specification'),)}),

        ('Especificação do Sistema Operacional', {
            'fields': (('sistem_operation',), ('sistem_specification',), ('user_sistem_operation', 'passwd_sistem_operation'),),  }),

        ('Especificação do Banco de Dados', {
            'fields': (('database_definition', 'database_version',),)}),

        ('Informações da Última Verificação', {
            'fields': (('last_verification', 'user_verification',),)}),
    )

    list_per_page = 50
    list_filter = ('companie',)
    search_fields = ('companie__name', 'memory_ram')
    save_as = True
    save_on_top = True
    show_full_result_count = True


admin.site.register(Servers,ServersAdmin)
