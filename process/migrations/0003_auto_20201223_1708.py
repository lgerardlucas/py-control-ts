# Generated by Django 2.2.2 on 2020-12-23 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_process_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='date_create',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Atualizada'),
        ),
    ]