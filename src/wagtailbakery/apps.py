from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig

from wagtailbakery.signal_handlers import register_signal_handlers


class WagtailBakeryAppConfig(AppConfig):
    name = 'wagtailbakery'
    label = 'wagtailbakery'
    verbose_name = "Wagtail bakery"

    def ready(self):
        register_signal_handlers()
