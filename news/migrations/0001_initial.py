# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('post', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
