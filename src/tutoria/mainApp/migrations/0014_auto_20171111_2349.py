# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_auto_20171031_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='subject_tags',
            field=models.ManyToManyField(blank=True, to='mainApp.Tag'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.University'),
        ),
    ]