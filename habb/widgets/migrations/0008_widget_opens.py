# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0007_widget_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='opens',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
