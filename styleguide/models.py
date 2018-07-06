from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

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

class ContentSection(CMSPlugin):
    CONTAINER_BACKGROUNDS = (
        ('#1c2532','navy'),
        ('#f3f4f5', 'light'),
        ('#ffffff', 'white')
    )

    background_color = models.CharField(choices = CONTAINER_BACKGROUNDS, default = 'white', max_length = 20)

class HeroBanner(CMSPlugin):
    TopLeftImageCircle = FilerImageField(null=True, blank=True, related_name="top_left_image", on_delete=models.SET_NULL)
    TopRightImageCircle = FilerImageField(null=True, blank=True, related_name="top_right_image", on_delete=models.SET_NULL)
    BottomRightImageCircle = FilerImageField(null=True, blank=True, related_name="bottom_left_image", on_delete=models.SET_NULL)
    BottomLeftImageCircle = FilerImageField(null=True, blank=True, related_name="bottom_right_image", on_delete=models.SET_NULL)

    HeroText = models.CharField(max_length=140, default="Accelerating progress toward understanding the brain.")

class NewsletterBox(CMSPlugin):
    call_to_action = models.CharField(default = "", max_length = 140)

class ApplicationTile(CMSPlugin):
    app_thumbnail = FilerImageField(null = True, blank = True, related_name="app_thumbnail", on_delete=models.SET_NULL)
    app_name = models.CharField(max_length = 50, default = "Cell Types Database")
    app_description = models.CharField(max_length = 140, default = "This section contains description copy for this Atlas or Database.")
    app_url = models.CharField(max_length = 1000, default = "http://celltypes.brain-map.org/")