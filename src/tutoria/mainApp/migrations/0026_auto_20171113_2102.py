# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mainApp', '0025_auto_20171113_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_mainapp.transaction_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_mainapp.tutor_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_mainapp.wallet_set+', to='contenttypes.ContentType'),
        ),
    ]
