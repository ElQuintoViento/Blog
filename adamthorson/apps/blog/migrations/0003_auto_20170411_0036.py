# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170411_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
