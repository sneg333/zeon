# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200306_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Book'),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]