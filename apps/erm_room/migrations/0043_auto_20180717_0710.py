# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-17 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0042_auto_20180710_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzleclue',
            name='clue_uploads_options',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='puzzlessummary',
            name='puzzle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_puzzles_spummary', to='erm_room.Puzzles'),
        ),
    ]