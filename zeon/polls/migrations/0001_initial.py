# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-05 11:32
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sobitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='текст события')),
                ('vrem_sobitie', models.DateTimeField(blank=True)),
            ],
            options={
                'verbose_name': 'события',
                'verbose_name_plural': 'события',
            },
        ),
    ]
