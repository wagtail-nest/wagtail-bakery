from bakery.views import BuildableDetailView
from wagtail.wagtailcore.middleware import SiteMiddleware
from wagtail.wagtailcore.models import Page, Site
from wagtail.wagtailcore.views import serve


class WagtailBakeryView(BuildableDetailView):
    """
    An abstract class that can be inherited to create a buildable view that can
    be added to BAKERY_VIEWS setting.
    """
    def get(self, request):
        middleware = SiteMiddleware()
        middleware.process_request(request)
        response = serve(request, request.path)
        return response

    def get_build_path(self, obj):
        return super(WagtailBakeryView, self).get_build_path(obj)

    def get_url(self, obj):
        return obj.url

    class Meta:
        abstract = True


class AllPublishedPagesView(WagtailBakeryView):
    """
    Generates a seperate index.html page for each published wagtail page.

    Example:
        # File: settings.py
        BAKERY_VIEWS = (
            'wagtailbakery.views.AllPublishedPagesView',
        )
    """
    def get_queryset(self):
        default_site = Site.objects.get(is_default_site=True)
        root_page = default_site.root_page
        return Page.objects.descendant_of(
            root_page, inclusive=True).public().live()
