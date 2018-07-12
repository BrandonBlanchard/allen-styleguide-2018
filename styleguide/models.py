from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from django.db import models



class ColorSwatch(CMSPlugin):
    color = models.CharField(max_length=6, default="343434")
    name = models.CharField(max_length=20, default="new color")
    sass_name = models.CharField(max_length=20, default="$newColor")

class FlexContainer(CMSPlugin):
    CONTAINER_SPACING_TYPES = (
        ("flex-start","flex-start"),
        ("flex-end","flex-end"),
        ("center","center"),
        ("space-between","space-between"),
        ("space-around","space-around"))
    
    CONTAINER_DIRECTION = (
        ("row", "Row"),
        ("row-reverse", "Row Reverse"),
        ("column", "Column"),
        ("column-reverse", "Column Reverse")
    )

    CONTAINER_WRAP = (
        ("wrap", "Wrap"),
        ("nowrap", "No Wrap"),
        ("wrao-reverse", "Wrap Reverse")
    )

    spacing = models.CharField(choices = CONTAINER_SPACING_TYPES, default = "flex-start", max_length = 13)
    direction = models.CharField(choices = CONTAINER_DIRECTION, default = "row", max_length = 20)
    wrap = models.CharField(choices = CONTAINER_WRAP, default = "wrap", max_length = 20)

class ContentSection(CMSPlugin):
    CONTAINER_BACKGROUNDS = (
        ("#1c2532","navy"),
        ("#f3f4f5", "light"),
        ("#ffffff", "white")
    )

    background_color = models.CharField(choices = CONTAINER_BACKGROUNDS, default = "white", max_length = 20)

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


class TypographicSample(CMSPlugin):
    FONT_TO_SAMPLE = (
        ("avenir-next", "Avenir Next"),
        ("roboto", "Roboto")
    )

    font_family = models.CharField(choices = FONT_TO_SAMPLE, default = "Roboto", max_length = 40)


class FlexColumn(CMSPlugin):
    COLUMN_WIDTH = (
        ("10%", "10%"),
        ("15%", "15%"),
        ("20%", "20%"),
        ("25%", "25%"),
        ("30%", "30%"),
        ("35%", "35%"),
        ("40%", "40%"),
        ("45%", "45%"),
        ("50%", "50%"),
        ("55%", "55%"),
        ("60%", "60%"),
        ("65%", "65%"),
        ("70%", "70%"),
        ("75%", "75%"),
        ("80%", "80%"),
        ("85%", "85%"),
        ("90%", "90%"),
        ("95%", "95%"),
        ("100%", "100%")
    )

    column_width = models.CharField(choices = COLUMN_WIDTH, default = "50%", max_length = 5)

class Button(CMSPlugin):
    BUTTON_COLOR = (
        ("blue","Blue"),
        ("green","Green"),
        ("yellow","Yellow"),
        ("black","Black"))
    
    BUTTON_STYLE = (
        ("primary", "Primary Button"),
        ("secondary", "Secondary Button"),
        ("compact", "Compact Button"),
        ("text", "Small Link"))

    label = models.CharField(default ="Click Me!", max_length = 140)
    url = models.CharField(default = "#", max_length = 2000)
    color = models.CharField(choices = BUTTON_COLOR, default = "Blue", max_length = 25)
    style = models.CharField(choices = BUTTON_STYLE, default = "Primary Button", max_length = 25)