# Generated by Django 2.2.4 on 2020-01-10 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0005_auto_20200110_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lowerthird',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='template', to='graphics.Template'),
        ),
    ]