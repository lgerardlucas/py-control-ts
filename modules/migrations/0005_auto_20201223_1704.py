# Generated by Django 2.2.2 on 2020-12-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_modules_system'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modules',
            options={'ordering': ['name', 'menu', 'system'], 'verbose_name': 'Módulo', 'verbose_name_plural': 'Módulos'},
        ),
        migrations.AlterField(
            model_name='modules',
            name='name',
            field=models.CharField(db_index=True, max_length=80, verbose_name='Módulo'),
        ),
    ]