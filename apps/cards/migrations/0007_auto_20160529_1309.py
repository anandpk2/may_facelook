# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 07:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_cards_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='related user'),
        ),
    ]
