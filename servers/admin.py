from django.contrib import admin
from .models import Servers,Information
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class InformationInline(admin.StackedInline): #TabularInline):
    model = Information

    max_num = 1 #Information.objects.all().count()

    list_display = ('get_server_nickname_companie', 'database_name', 
                    'get_database_size_database_size_initials',

                    'get_hd_size_one_hd_size_one_initials',
                    'get_hd_size_one_available_hd_size_one_available_initials',

                    'get_hd_size_two_hd_size_two_initials',
                    'get_hd_size_two_available_hd_size_two_available_initials',

                    'verification_data')

    fieldsets = (
        ('Empresa Proprietária', {
            'fields': (('server',),)}),
        ('Informações do Banco de Dados', {
            'fields': (('database_name'), ('database_size', 'database_size_initials'),)}),
        ('Dados do Disco - Sistema Operacional', {
            'fields': (('hd_size_one', 'hd_size_one_available'),)}),
        ('Dados do Disco - Banco de Dados', {
            'fields': (('hd_size_two', 'hd_size_two_available'),)}),
        ('Informações da Última Verificação', {
            'fields': (('last_verification', 'user_verification',),)}),
    )

class InformationAdmin(admin.ModelAdmin):
    list_display = ('get_server_nickname_companie', 'database_name', 'get_sistem_operation',
                    'get_database_size_database_size_initials',

                    'get_hd_size_one_hd_size_one_initials',
                    'get_hd_size_one_available_hd_size_one_available_initials',

                    'get_hd_size_two_hd_size_two_initials',
                    'get_hd_size_two_available_hd_size_two_available_initials',

                    'verification_data')
                        
    fieldsets = (
        ('Empresa Proprietária', {
            'fields': (('server',),)}),
        ('Informações do Banco de Dados', {
            'fields': (('database_name'), ('database_size', 'database_size_initials'),)}),
        ('Dados do Disco - Sistema Operacional', {
            'fields': (('hd_size_one', 'hd_size_one_available'),)}),
        ('Dados do Disco - Banco de Dados', {
            'fields': (('hd_size_two', 'hd_size_two_available'),)}),
        ('Informações da Última Verificação', {
            'fields': (('last_verification', 'user_verification',),)}),
    )
    list_per_page = 50
    list_filter = ('server__companie__nickname',)
    search_fields = ('database_name', 'server__companie__name',
                     'server__companie__nickname')
    save_as = True
    save_on_top = True
    show_full_result_count = True


admin.site.register(Information, InformationAdmin)


class ServersAdmin(admin.ModelAdmin):
    list_display = ('get_nickname_companie', 'ip_network', 'sistem_operation', 'sistem_specification',
                    'get_memory_ram_initial', 'partition_size_specification', 'database_definition', 'database_version', 'validate_verification')
    fieldsets = (
        ('Empresa Proprietária', {
            'fields': (('companie',),)}),

        ('Especificação do Servidor', {
            'fields': (('processor'), ('memory_ram', 'ip_network'), ('partition_size_specification', 'machine_type',), (('provider_acquisition','date_acquisition')),)}),

        ('Especificação do Sistema Operacional', {
            'fields': (('sistem_operation', 'virtual_machine',), ('sistem_specification',), ('user_sistem_operation', 'passwd_sistem_operation'),), }),

        ('Especificação do Banco de Dados', {
            'fields': (('database_definition', 'database_version',),)}),

        ('Informações da Última Verificação', {
            'fields': (('last_verification', 'user_verification',),)}),
    )
    inlines = (InformationInline,)
    list_per_page = 50
    list_filter = ('companie', 'sistem_operation')
    search_fields = ('companie__name', 'companie__nickname','memory_ram',
                     'sistem_operation', 'ip_network')
    save_as = True
    save_on_top = True
    show_full_result_count = True

admin.site.register(Servers, ServersAdmin)



