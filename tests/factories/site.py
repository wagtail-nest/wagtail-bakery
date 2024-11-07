import factory
from wagtail.models import Site


class SiteFactory(factory.django.DjangoModelFactory):
    hostname = "localhost"
    port = 80
    is_default_site = True

    class Meta:
        model = Site
        django_get_or_create = ("hostname", "port")
