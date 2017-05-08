# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 03:21
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0009_challenge_code_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='test_key',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='challenge_files',
            field=models.FileField(default='e:\\Git\\machine-learning-capstone\\django\\Website\\Website\\z_Media\\challenges\\challenge_avis\\default.zip', max_length=300, storage=django.core.files.storage.FileSystemStorage(location='e:\\Git\\machine-learning-capstone\\django\\Website\\Website\\z_Media\\challenges\\'), upload_to=''),
        ),
    ]