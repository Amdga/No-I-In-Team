# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-13 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trimit', '0011_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='mean_atmosphere_rating',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='mean_price_rating',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='mean_service_rating',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='number_of_reviews',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='overall_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, null=True),
        ),
    ]
