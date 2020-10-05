import wagtail

if wagtail.VERSION >= (2, 8):
    from wagtail.api.v2.views import PagesAPIViewSet  # noqa: F401
else:
    from wagtail.api.v2.endpoints import PagesAPIEndpoint as PagesAPIViewSet  # noqa: F401
