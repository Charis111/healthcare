# Generated by Django 3.0.4 on 2020-05-30 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200530_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorfullprofile',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 18, 29, 34, 902824), verbose_name='date published'),
        ),
    ]
