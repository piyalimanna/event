# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-02 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sa',
        ),
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
