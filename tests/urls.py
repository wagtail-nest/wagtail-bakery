from django.urls import include, path
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.admin import urls as wagtailadmin_urls

if WAGTAIL_VERSION >= (3, 0):
    from wagtail import urls as wagtail_urls
else:
    from wagtail.core import urls as wagtail_urls

urlpatterns = [
    path('admin/', include(wagtailadmin_urls)),
    path('', include(wagtail_urls)),
]
