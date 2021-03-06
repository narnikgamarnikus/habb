# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0013_auto_20171109_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='winner',
        ),
        migrations.RemoveField(
            model_name='widget',
            name='competition',
        ),
        migrations.AddField(
            model_name='widget',
            name='competition_status',
            field=models.CharField(blank=True, choices=[('soon', 'Coming soon'), ('active', 'Active'), ('complete', 'Complete')], default='soon', max_length=20),
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
    ]
