# Generated by Django 3.1.2 on 2020-12-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0006_auto_20201217_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockpunch',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]