# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 21:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('widgets', '0012_auto_20171031_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='widget',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='widgets.Website'),
        ),
    ]
