# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=255)),
                ('card_description', models.TextField(verbose_name='card_description')),
                ('card_created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]
