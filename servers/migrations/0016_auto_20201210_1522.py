# Generated by Django 2.2.2 on 2020-12-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0015_auto_20201210_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='database_size',
            field=models.FloatField(blank=True, null=True, verbose_name='Tamanho do Banco'),
        ),
    ]
