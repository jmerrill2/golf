# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='volume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scripture.Volume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scripture.Book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verse',
            name='chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scripture.Chapter'),
            preserve_default=False,
        ),
    ]
