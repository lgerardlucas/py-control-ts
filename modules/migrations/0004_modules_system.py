# Generated by Django 2.2.2 on 2020-12-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0003_remove_systems_module'),
        ('modules', '0003_auto_20201221_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='system',
            field=models.ForeignKey(default=1, on_delete=False, related_name='system_module', to='systems.Systems', verbose_name='Sistema'),
            preserve_default=False,
        ),
    ]