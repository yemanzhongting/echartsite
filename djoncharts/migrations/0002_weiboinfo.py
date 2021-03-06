# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-02-21 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djoncharts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeiboInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('vis', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('idinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djoncharts.AddressInfo')),
            ],
            options={
                'verbose_name': '微博信息',
                'verbose_name_plural': '微博信息',
                'db_table': 'weiboinfo',
            },
        ),
    ]
