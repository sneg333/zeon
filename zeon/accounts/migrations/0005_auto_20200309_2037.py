# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20200309_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, verbose_name='о себе')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('pol', models.CharField(blank=True, choices=[('m', 'мужской'), ('g', 'женский')], max_length=100, verbose_name='пол')),
                ('statstar', models.CharField(blank=True, choices=[('a', 'в отношениях'), ('b', 'свободен')], max_length=100, verbose_name='статус')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'профиль пользователя',
                'verbose_name_plural': 'профиль пользователя',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
