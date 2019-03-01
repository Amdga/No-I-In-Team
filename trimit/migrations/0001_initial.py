# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-01 00:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialities', models.CharField(blank=True, max_length=30, null=True)),
                ('flat_number', models.CharField(blank=True, max_length=15)),
                ('street_address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('postcode', models.CharField(blank=True, max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('opening_times', models.CharField(blank=True, max_length=200, null=True)),
                ('webpage', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='hairpage_images')),
                ('contact_number', models.CharField(blank=True, max_length=15)),
                ('latitude', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=9)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('atmosphere_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('price_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('service_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trimit.Page')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='user_profile_images')),
                ('hairpicture', models.ImageField(blank=True, upload_to='user_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trimit.UserProfile'),
        ),
    ]
