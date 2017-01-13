# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-13 12:07
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=blog.models.get_image_path, verbose_name='Thumbnail'),
        ),
    ]