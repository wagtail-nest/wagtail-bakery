import factory

from wagtail.wagtailcore.models import Site


class SiteFactory(factory.DjangoModelFactory):
    hostname = 'localhost'
    port = 80
    is_default_site = True

    class Meta:
        model = Site
        django_get_or_create = ('hostname', 'port')
