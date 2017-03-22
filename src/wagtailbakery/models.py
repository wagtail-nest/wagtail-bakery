from bakery.models import BuildableModel

from wagtailbakery.views import WagtailBakeryView


class BuildableWagtailBakeryModel(BuildableModel):
    """
    Buildable Wagtail bakery page model mixin class.
    """
    detail_views = (WagtailBakeryView,)

    def _build_related(self):
        # TODO: Build related pages with get_static_site_paths
        pass

    class Meta:
        abstract = True


class AutoPublishingWagtailBakeryModel(BuildableWagtailBakeryModel):
    """
    Auto publishing Wagtail bakery page model mixin class.
    """
    publication_status_field = 'live'

    def save(self, *args, **kwargs):
        super(AutoPublishingWagtailBakeryModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
