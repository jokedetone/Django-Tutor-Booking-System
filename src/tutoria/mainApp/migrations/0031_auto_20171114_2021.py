# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0030_auto_20171114_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiontransaction',
            name='commission',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]
