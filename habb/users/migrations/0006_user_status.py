# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('free', 'Free'), ('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold')], default='free', max_length=20),
        ),
    ]