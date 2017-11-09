# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-31 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0010_auto_20171030_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('status', model_utils.fields.StatusField(choices=[('active', 'Active'), ('complete', 'Complete')], default='active', max_length=20, no_check_for_status=True)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widgets.Leed')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='widget',
            name='competition_type',
            field=models.CharField(choices=[('random', 'Random'), ('leeds', 'Leeds')], default='random', max_length=20),
        ),
        migrations.AlterField(
            model_name='widget',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='widgets.Competition'),
        ),
    ]