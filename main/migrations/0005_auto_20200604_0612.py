# Generated by Django 3.0.4 on 2020-06-04 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200530_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorfullprofile',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 4, 6, 12, 55, 394890), verbose_name='date published'),
        ),
    ]