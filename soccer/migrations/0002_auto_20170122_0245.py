# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goalkeepercareerstatistics',
            options={'verbose_name_plural': 'goalkeeper career statistics'},
        ),
        migrations.AlterModelOptions(
            name='goalkeepercompetitionstatistics',
            options={'verbose_name_plural': 'goalkeeper competition statistics'},
        ),
        migrations.AlterModelOptions(
            name='goalscored',
            options={'verbose_name_plural': 'goals scored'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AlterModelOptions(
            name='outfieldplayercareerstatistics',
            options={'verbose_name_plural': 'outfield player career statistics'},
        ),
        migrations.AlterModelOptions(
            name='outfieldplayercompetitionstatistics',
            options={'verbose_name_plural': 'outfield player competition statistics'},
        ),
        migrations.AlterModelOptions(
            name='teamalltimestatistics',
            options={'verbose_name_plural': 'team all time statistics'},
        ),
        migrations.AlterModelOptions(
            name='teamcompetitionstatistics',
            options={'verbose_name_plural': 'team competition statistics'},
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.CharField(blank=True, choices=[('home', 'home'), ('away', 'away')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
