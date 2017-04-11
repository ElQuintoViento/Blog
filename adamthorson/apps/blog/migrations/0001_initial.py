# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('publish_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('owner', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('tags', models.ManyToManyField(to='core.Tag', blank=True, related_name='series')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='series',
            field=models.ForeignKey(to='blog.Series'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='core.Tag', blank=True, related_name='posts'),
        ),
    ]
