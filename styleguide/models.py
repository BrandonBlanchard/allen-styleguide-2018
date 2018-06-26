from cms.models.pluginmodel import CMSPlugin

from django.db import models



class ColorSwatch(CMSPlugin):
    color = models.CharField(max_length=6, default='343434')
    name = models.CharField(max_length=20, default='new color')
    sass_name = models.CharField(max_length=20, default='$newColor')