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

    def get_site(self):
        """Return the site were to build the static pages from.

        By default this is the site marked as default with `is_default_site`
        set to `true`.

        Example:
            def get_site(self):
                return Site.objects.get(hostname='website.com')
        """
        return Site.objects.get(is_default_site=True)

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
        site = self.get_site()
        root_page = site.root_page
        descendants = Page.objects.descendant_of(root_page, inclusive=True)
        return descendants.public().live()
