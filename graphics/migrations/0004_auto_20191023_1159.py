# Generated by Django 2.2.4 on 2019-10-23 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0003_auto_20191023_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lowerthird',
            old_name='title',
            new_name='_title',
        ),
    ]
