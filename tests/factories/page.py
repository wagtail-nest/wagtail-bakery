import factory
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page


class PageFactory(factory.DjangoModelFactory):
    depth = 2
    numchild = 0
    path = '00010002'
    title = 'Page'
    slug = 'page'
    url_path = '/page/'

    class Meta:
        model = Page
