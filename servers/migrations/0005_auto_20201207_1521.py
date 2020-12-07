# Generated by Django 2.2.2 on 2020-12-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20201207_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='database_definition',
            field=models.CharField(blank=True, choices=[('PosgreSQL', 'PostgreSQL'), ('Outros', 'Outros')], default='PostgreSQL', max_length=20, null=True, verbose_name='Banco de Dados'),
        ),
    ]
