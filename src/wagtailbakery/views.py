import logging
import os

from bakery.views import BuildableDetailView
from django.conf import settings
from django.core.handlers.base import BaseHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.test.client import RequestFactory
from django.utils.six.moves.urllib.parse import urlparse
from wagtail.wagtailcore.models import Page, Site

logger = logging.getLogger(__name__)


class WagtailBakeryView(BuildableDetailView):
    """
    An abstract class that can be inherited to create a buildable view that can
    be added to BAKERY_VIEWS setting.
    """
    def __init__(self, *args, **kwargs):
        self.handler = BaseHandler()
        self.handler.load_middleware()

        super(WagtailBakeryView, self).__init__(*args, **kwargs)

    def get(self, request):
        response = self.handler.get_response(request)
        return response

    def get_content(self, obj):
        response = self.get(self.request)
        if isinstance(response, HttpResponseRedirect):
            return self.get_redirect_content(response, obj)
        if hasattr(response, 'render'):
            return response.render().content
        if hasattr(response, 'content'):
            return response.content
        raise AttributeError(
            "'%s' object has no attribute 'render' or 'content'" % response)

    def get_redirect_content(self, response, obj):
        context = {
            'page': obj,
            'self': obj,
            'redirect_url': response.url,
        }
        content = render(
            self.request, 'wagtailbakery/redirect.html', context).content
        return response.make_bytes(content)

    def get_build_path(self, obj):
        url = self.get_url(obj)

        if url.startswith('http'):
            # Multisite has absolute urls
            url_parsed = urlparse(url)
            path = url_parsed.path
            hostname = url_parsed.hostname

            if getattr(settings, 'BAKERY_MULTISITE', False):
                build_path = os.path.join(
                    settings.BUILD_DIR, hostname, path[1:])
            else:
                build_path = os.path.join(settings.BUILD_DIR, path[1:])
        else:
            # Single site has relative urls
            build_path = os.path.join(settings.BUILD_DIR, url[1:])

        # Make sure the (deeply) directories are created
        os.path.exists(build_path) or os.makedirs(build_path)

        # Always append index.html at the end of the path
        return os.path.join(build_path, 'index.html')

    def get_url(self, obj):
        """Return Wagtail page url instead of Django's get_absolute_url."""
        return obj.url

    def get_path(self, obj):
        """Return Wagtail path to page."""
        return obj.path

    def build_object(self, obj):
        """
        Build wagtail page and set SERVER_NAME to retrieve corresponding site
        object.
        """
        site = obj.get_site()
        logger.debug("Building %s" % obj)
        self.request = RequestFactory(
            SERVER_NAME=site.hostname).get(self.get_url(obj))
        self.set_kwargs(obj)
        path = self.get_build_path(obj)
        self.build_file(path, self.get_content(obj))

    def build_queryset(self):
        for item in self.get_queryset().all():
            url = self.get_url(item)
            if url is not None:
                self.build_object(item)

    class Meta:
        abstract = True


class AllPagesView(WagtailBakeryView):
    """
    Generates a seperate index.html page for each (latest revision) wagtail
    page.

    Use this view to export your pages for acceptance/staging environments.

    Example:
        # File: settings.py
        BAKERY_VIEWS = (
            'wagtailbakery.views.AllPagesView',
        )
    """
    def get_queryset(self):
        if getattr(settings, 'BAKERY_MULTISITE', False):
            return Page.objects.all().public()
        else:
            site = Site.objects.get(is_default_site=True)
            return site.root_page.get_descendants(inclusive=True).public()


class AllPublishedPagesView(AllPagesView):
    """
    Generates a seperate index.html page for each published wagtail page.

    Use this view to export your pages for production.

    Example:
        # File: settings.py
        BAKERY_VIEWS = (
            'wagtailbakery.views.AllPublishedPagesView',
        )
    """
    def get_queryset(self):
        pages = super(AllPublishedPagesView, self).get_queryset()
        return pages.live()
