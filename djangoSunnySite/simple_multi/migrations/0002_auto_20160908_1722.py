# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_multi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='attachments'),
        ),
    ]