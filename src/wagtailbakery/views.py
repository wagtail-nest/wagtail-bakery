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
        root_path = Site.get_site_root_paths()
        if len(root_path):
            root_path = root_path[0][1]
            if obj.url_path == root_path:
                return '/'
            elif root_path in obj.url_path:
                if obj.url_path.index(root_path) == 0:
                    return obj.url.replace(root_path, '/', 1)
        return obj.url_path

    class Meta:
        abstract = True


class AllPublishedPagesView(WagtailBakeryView):
    """
    Generates a seprate index.html page for each published wagtail page.

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
