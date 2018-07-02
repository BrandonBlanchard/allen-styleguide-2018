# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('styleguide', '0002_flexcontainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='styleguide_contentsection', serialize=False, to='cms.CMSPlugin')),
                ('background_color', models.CharField(choices=[('navy', '#1c2532'), ('light', '#f3f4f5'), ('white', '#ffffff')], default='white', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='flexcontainer',
            name='spacing',
            field=models.CharField(choices=[('flex-start', 'flex-start'), ('flex-end', 'flex-end'), ('center', 'center'), ('space-between', 'space-between'), ('space-around', 'space-around')], default='flex-start', max_length=13),
        ),
    ]