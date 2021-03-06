# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0008_widget_opens'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widget',
            old_name='opens',
            new_name='closed',
        ),
        migrations.RenameField(
            model_name='widget',
            old_name='views',
            new_name='opened',
        ),
        migrations.AddField(
            model_name='widget',
            name='viewed',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
