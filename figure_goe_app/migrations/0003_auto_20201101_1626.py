# Generated by Django 3.0 on 2020-11-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figure_goe_app', '0002_auto_20201101_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jump',
            old_name='free_or_short',
            new_name='event',
        ),
    ]
