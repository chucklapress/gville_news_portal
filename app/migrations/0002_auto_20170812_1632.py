# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-12 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessarticle',
            name='other_business_today',
        ),
        migrations.RemoveField(
            model_name='headlinearticle',
            name='second_lede_today',
        ),
        migrations.RemoveField(
            model_name='headlinearticle',
            name='third_lede_today',
        ),
        migrations.RemoveField(
            model_name='localarticle',
            name='other_local_today',
        ),
        migrations.RemoveField(
            model_name='sportsarticle',
            name='other_sports_today',
        ),
    ]
