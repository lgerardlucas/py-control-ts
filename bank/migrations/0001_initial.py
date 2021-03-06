# Generated by Django 2.2.2 on 2021-01-05 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0008_auto_20201223_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(blank=True, choices=[('Banco do Brasil - 001', 'Banco do Brasil - 001'), ('Banrisul - 041', 'Banrisul - 041'), ('CEF - 104', 'CEF - 104'), ('Itáu - 341', 'Itáu - 341'), ('Santander - 033', 'Santander - 033'), ('Sicredi - 748', 'Sicredi - 748')], default='Outros', max_length=20, null=True, verbose_name='Banco')),
                ('enable_bank', models.BooleanField(default=True, verbose_name='Ativo')),
                ('date_update', models.DateField(auto_now=True, null=True, verbose_name='Cadastro')),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Atualizada')),
                ('cedante_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cód/Cedente')),
                ('agency', models.CharField(blank=True, max_length=10, null=True, verbose_name='Agência')),
                ('account', models.CharField(blank=True, max_length=50, null=True, verbose_name='Conta Corrente')),
                ('companie', models.ForeignKey(on_delete=False, related_name='empresa_bank', to='companies.Companies', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Remessa Bancária',
                'verbose_name_plural': 'Remessas Bancárias',
                'ordering': ['bank'],
            },
        ),
    ]
