# Generated by Django 2.2.2 on 2021-01-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_auto_20210105_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='date_inactive',
            field=models.DateField(blank=True, null=True, verbose_name='Inativado'),
        ),
    ]