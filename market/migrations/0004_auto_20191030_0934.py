# Generated by Django 2.2.6 on 2019-10-30 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20191025_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='title',
            new_name='department',
        ),
    ]
