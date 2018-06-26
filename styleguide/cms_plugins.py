from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import ColorSwatch

@plugin_pool.register_plugin
class ColorSwatchPlugin(CMSPluginBase):
    model = ColorSwatch
    name = _("Color Swatch")
    render_template = "swatch.html"
    cache = False

    def render (self, context, instance, placeholder):
        context = super(ColorSwatchPlugin, self).render(context, instance, placeholder)
        return context

