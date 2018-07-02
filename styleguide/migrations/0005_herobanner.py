# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 21:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0020_old_tree_cleanup'),
        ('styleguide', '0004_auto_20180627_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroBanner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='styleguide_herobanner', serialize=False, to='cms.CMSPlugin')),
                ('HeroText', models.CharField(default='Accelerating progress toward understanding the brain.', max_length=140)),
                ('BottomLeftImageCircle', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottom_right_image', to=settings.FILER_IMAGE_MODEL)),
                ('BottomRightImageCircle', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottom_left_image', to=settings.FILER_IMAGE_MODEL)),
                ('TopLeftImageCircle', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top_left_image', to=settings.FILER_IMAGE_MODEL)),
                ('TopRightImageCircle', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top_right_image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
