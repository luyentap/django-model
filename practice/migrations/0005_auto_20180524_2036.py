# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 13:36
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_product_number'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]