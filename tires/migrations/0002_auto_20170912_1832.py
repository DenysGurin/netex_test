# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tires', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
