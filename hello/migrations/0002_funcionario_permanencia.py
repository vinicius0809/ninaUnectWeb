# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-04 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('ra', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('rfid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permanencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('saida', models.DateTimeField(blank=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Funcionario')),
            ],
        ),
    ]
