# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 06:24
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20170407_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenge_files',
            field=models.FileField(default='c:\\Git\\machine-learning-capstone\\django\\Website\\Website\\z_Media\\challengesdefault.txt', storage=django.core.files.storage.FileSystemStorage(location='c:\\Git\\machine-learning-capstone\\django\\Website\\Website\\z_Media\\challenges\\'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='challenge_image',
            field=models.ImageField(default='c:\\Git\\machine-learning-capstone\\django\\Website\\Website\\z_Media\\challenge_avisdefault.jpg', storage=django.core.files.storage.FileSystemStorage(location='c:\\Git\\machine-learning-capstone\\django\\Website\\Website\\z_Media\\challenge_avis\\'), upload_to=''),
        ),
    ]
