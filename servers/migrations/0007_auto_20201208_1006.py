# Generated by Django 2.2.2 on 2020-12-08 13:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0006_auto_20201208_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='user_verification',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, related_name='user_information', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
