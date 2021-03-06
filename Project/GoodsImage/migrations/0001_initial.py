# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-24 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='图片编号')),
                ('path', models.ImageField(blank=True, null=True, upload_to='static/images/GoodsImage/', verbose_name='图片路径')),
                ('status', models.BooleanField(default=True, verbose_name='默认展示')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='所属商品')),
            ],
        ),
    ]
