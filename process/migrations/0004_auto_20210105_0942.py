# Generated by Django 2.2.2 on 2021-01-05 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_auto_20201223_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='process',
            options={'ordering': ['title'], 'verbose_name': 'Processo - Suporte', 'verbose_name_plural': 'Processos - Suporte'},
        ),
    ]
