# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenge_image',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='home.Picture'),
        ),
    ]
