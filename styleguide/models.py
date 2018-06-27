from cms.models.pluginmodel import CMSPlugin

from django.db import models



class ColorSwatch(CMSPlugin):
    color = models.CharField(max_length=6, default='343434')
    name = models.CharField(max_length=20, default='new color')
    sass_name = models.CharField(max_length=20, default='$newColor')

class FlexContainer(CMSPlugin):
    CONTAINER_SPACING_TYPES = (
        ('flex-start','flex-start'),
        ('flex-end','flex-end'),
        ('center','center'),
        ('space-between','space-between'),
        ('space-around','space-around'))
    
    spacing = models.CharField(choices = CONTAINER_SPACING_TYPES, default = 'flex-start', max_length = 13)