# Generated by Django 2.2.2 on 2020-12-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0007_auto_20201208_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='hd_size_one_available',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tam/Disco Disp(SO)'),
        ),
        migrations.AddField(
            model_name='information',
            name='hd_size_two_available',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tam/Disc Disp(BD)'),
        ),
        migrations.AlterField(
            model_name='information',
            name='hd_size_one',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tam/Disco(SO)'),
        ),
    ]