# Generated by Django 2.2.2 on 2020-12-21 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_systems_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systems',
            name='module',
        ),
    ]