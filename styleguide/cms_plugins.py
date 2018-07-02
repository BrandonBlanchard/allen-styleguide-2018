from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import ColorSwatch, FlexContainer, ContentSection, HeroBanner

@plugin_pool.register_plugin
class ColorSwatchPlugin(CMSPluginBase):
    model = ColorSwatch
    name = _("Color Swatch")
    render_template = "swatch.html"
    cache = False

    def render (self, context, instance, placeholder):
        context = super(ColorSwatchPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class FlexContainerPlugin(CMSPluginBase):
    model = FlexContainer
    name = _("Flex Container")
    render_template = "flex-container.html"
    allow_children = True
    cache = False

    def render (self, context, instance, placeholder):
        context = super(FlexContainerPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ContentSectionPlugin(CMSPluginBase):
    model = ContentSection
    name = _("Content Section")
    render_template = 'section-content.html'
    allow_children = True
    cache = False

    def render (self, context, instance, placeholder):
        context = super(ContentSectionPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class HeroBannerPlugin(CMSPluginBase):
    model = HeroBanner
    name = _("Hero Banner")
    render_template = 'hero-banner.html'
    allow_children = False
    cache = False

    def render (self, context, instance, placeholder):
        context = super(HeroBannerPlugin, self).render(context, instance, placeholder)
        return context