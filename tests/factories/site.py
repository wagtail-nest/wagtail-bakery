import factory
import wagtail
if wagtail.VERSION >= (2, 0):
    from wagtail.core.models import Site
else:
    from wagtail.wagtailcore.models import Site


class SiteFactory(factory.DjangoModelFactory):
    hostname = 'localhost'
    port = 80
    is_default_site = True

    class Meta:
        model = Site
        django_get_or_create = ('hostname', 'port')
