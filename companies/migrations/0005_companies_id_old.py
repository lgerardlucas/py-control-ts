# Generated by Django 2.2.2 on 2020-12-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20201204_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='id_old',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID Sistem Antigo'),
        ),
    ]
