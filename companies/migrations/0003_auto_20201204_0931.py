# Generated by Django 2.2.2 on 2020-12-04 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20201204_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='stret_number',
            new_name='street_number',
        ),
    ]