import factory
from wagtail.wagtailredirects.models import Redirect

from tests.factories.page import PageFactory
from tests.factories.site import SiteFactory


class RedirectFactory(factory.DjangoModelFactory):
    old_path = '/old/'
    site = factory.SubFactory(SiteFactory)
    redirect_page = factory.SubFactory(PageFactory)

    class Meta:
        model = Redirect
