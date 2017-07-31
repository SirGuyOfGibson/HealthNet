# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-31 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20170721_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('startDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('duration', models.DurationField(default=0)),
                ('instructions', models.CharField(max_length=1000, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('endDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('height', models.CharField(max_length=1000, null=True)),
                ('weight', models.CharField(max_length=1000, null=True)),
                ('blood_pressure', models.CharField(max_length=1000, null=True)),
                ('heart_rate', models.CharField(max_length=1000, null=True)),
                ('respirations_minute', models.CharField(max_length=1000, null=True)),
                ('reason', models.CharField(max_length=1000, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=80)),
                ('comments', models.CharField(max_length=100)),
                ('released', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
            ],
        ),
    ]
