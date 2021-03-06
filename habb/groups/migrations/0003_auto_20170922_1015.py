# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-22 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20170915_1214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterField(
            model_name='group',
            name='group_map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Map', verbose_name='Карта'),
        ),
        migrations.AlterField(
            model_name='group',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='group',
            name='servser',
            field=models.CharField(max_length=50, verbose_name='Сервер'),
        ),
        migrations.AlterField(
            model_name='group',
            name='team',
            field=models.ManyToManyField(to='teams.Team', verbose_name='Комманды'),
        ),
    ]
