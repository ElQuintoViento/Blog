# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='series',
            field=models.ForeignKey(null=True, blank=True, to='blog.Series'),
        ),
    ]
