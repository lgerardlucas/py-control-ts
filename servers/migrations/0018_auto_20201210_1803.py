# Generated by Django 2.2.2 on 2020-12-10 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0017_auto_20201210_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='last_verification',
            field=models.DateField(blank=True, default=datetime.date(2020, 12, 10), null=True, verbose_name='Última Verificação'),
        ),
    ]