# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='อาจารย์อยาได้อะไรค้าบ',
            field=models.CharField(default='ไม่บอก', max_length=20),
        ),
    ]
