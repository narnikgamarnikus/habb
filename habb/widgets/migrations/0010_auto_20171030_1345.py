# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-30 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0009_auto_20170925_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widget',
            old_name='competitions',
            new_name='competition',
        ),
    ]