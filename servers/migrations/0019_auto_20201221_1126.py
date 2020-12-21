# Generated by Django 2.2.2 on 2020-12-21 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0018_auto_20201210_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='last_verification',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 21, 13, 26, 1, 98782, tzinfo=utc), null=True, verbose_name='Última Verificação'),
        ),
        migrations.AlterField(
            model_name='servers',
            name='last_verification',
            field=models.DateField(blank=True, default=datetime.date(2020, 12, 21), null=True, verbose_name='Última Verificação'),
        ),
    ]
