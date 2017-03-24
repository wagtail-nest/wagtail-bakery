from bakery.models import AutoPublishingBuildableModel, BuildableModel

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


class AutoPublishingWagtailBakeryModel(AutoPublishingBuildableModel):
    """
    Auto publishing Wagtail bakery page model mixin class.
    """
    detail_views = (WagtailBakeryView,)
    publication_status_field = 'live'

    def _build_related(self):
        # TODO: Build related pages with get_static_site_paths
        pass

    class Meta:
        abstract = True
